from typing import *
from types import *


class Video:
    def __init__(self, id: int, size):
        self.id = id
        self.size = size


class Cache:
    def __init__(self, id: int, capacity):
        self.id = id
        self.capacity = capacity
        self.current_capacity = 0


class Endpoint:
    def __init__(self, id: int, dc_latency, caches_latency: Dict[Cache, int]):
        self.id = id
        self.dc_latency = dc_latency
        self.caches_latency = caches_latency


class Request:
    def __init__(self, endpoint: Endpoint, video: Video, reqs: int):
        self.endpoint = endpoint
        self.video = video
        self.reqs = reqs


class Problem:
    def __init__(self,
                 V: int,
                 E: int,
                 R: int,
                 C: int,
                 X: int,
                 videos: List[Video],
                 endpoints: List[Endpoint],
                 caches: List[Cache],
                 requests: List[Request]):
        self.V = V
        self.E = E
        self.R = R
        self.C = C
        self.X = X
        self.videos = videos
        self.endpoints = endpoints
        self.caches = caches
        self.requests = requests

