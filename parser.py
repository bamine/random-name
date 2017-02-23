from typing import *
from types import *


class Video:
    def __init__(self, id: int, size):
        self.id = id
        self.size = size


class Endpoint:
    def __init__(self, id: int, dc_latency, caches: Dict[Cache, int]):
        self.id = id
        self.dc_latency = dc_latency
        self.caches = caches


class Cache:
    def __init__(self, id: int, capacity):
        self.id = id
        self.capacity = capacity


class Request:
    def __init__(self, id: int, endpoint: Endpoint, video: Video, reqs: int):
        self.id = id
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