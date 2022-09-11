
# IPFS FASTAPI Authenticated Reverse Proxy

Reverse Proxy server for ipfs http client with authentication of Token/IP Address.



## ⚠️ Note

IP Authorization wont work if you are using Nginx's Proxy Pass . I will add a support for it in future if i ever need it.


## Installation


Start up the server using the commands below : 

Note : Edit config.json to manage tokens and other settings

```bash
  git clone https://github.com/dineshtiwari69/authenticated-ipfs-reverse-proxy
  cd authenticated-ipfs-reverse-proxy
  pip install -r requirements.txt
  uvicorn core:app --reload
```
    
## Usage/Examples with ipfs-http-client

```javascript
import { create } from 'ipfs-http-client'

const ipfs = create({
  host: 'localhost',
  port: 8000,
  protocol: 'http',
  headers: {
    authorization: 'Your TOKEN'
  }
})
```

