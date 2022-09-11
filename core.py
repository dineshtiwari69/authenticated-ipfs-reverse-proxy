from starlette.requests import Request
from starlette.responses import StreamingResponse
from starlette.background import BackgroundTask
from fastapi import FastAPI,Request,HTTPException
import httpx
from utils.utils import get_config

app = FastAPI()

IPFS_NODE = get_config().ipfs_node

client = httpx.AsyncClient(base_url=IPFS_NODE)

async def _reverse_proxy(request: Request):
    """

        Reverse Proxy using Fast API
        https://github.com/tiangolo/fastapi/issues/1788#issuecomment-1071222163

    
    """
    url = httpx.URL(path=request.url.path,
                    query=request.url.query.encode("utf-8"))
    config = get_config()
    

    auth_token = request.headers.get("Authorization")
    ip_addr = request.client.host
    if config.ip_filter and (ip_addr not in config.ip_allowlist):
        raise HTTPException(status_code=401,detail="IP Address not authorized")
    if config.require_token and (auth_token not in config.tokens):
        raise HTTPException(status_code=401,detail="Invalid Token")
    rp_req = client.build_request(request.method, url,
                                  headers=request.headers.raw,
                                  content=await request.body())
    rp_resp = await client.send(rp_req, stream=True)
    return StreamingResponse(
        rp_resp.aiter_raw(),
        status_code=rp_resp.status_code,
        headers=rp_resp.headers,
        background=BackgroundTask(rp_resp.aclose),
    )

app.add_route("/{path:path}",_reverse_proxy, ["GET", "POST","PUT","DELETE"])


