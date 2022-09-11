

import json 
from dataclasses import dataclass,field,fields
from typing import List
from dacite import from_dict


@dataclass
class Config:
    ipfs_node: str = ""
    tokens: List[str] = field(default_factory=lambda: [''])
    ip_allowlist: List[str]  = field(default_factory=lambda: [''])
    require_token: bool = False
    ip_filter: bool = False


def get_config()->Config:
    try:
        with open("config.json","r") as f:
            data=json.load(f)
        return from_dict(data_class=Config,data=data)
    except Exception:
        return Config()




