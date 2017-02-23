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


def parse(inFile):
    inF = open(inFile, 'r')
    l1 = inF.readline().rstrip().split(' ')
    (V, E, R, C, X) = [int(i) for i in l1]

    l2 = inF.readline().rstrip().split(' ')
    zipV= zip(range(len(l2)), l2)
    videos = [Video(x[0], x[1]) for x in zipV]
    videos_dict = {}
    for v in videos:
        videos_dict[v.id] = v
    assert(len(videos)==V)

    endpoints = []
    id_endpoint = 0
    for endp in range(E):
        (latency, nb_caches) = [int(k) for k in inF.readline().rstrip().split(' ')]
        dic_caches = {}
        for cache in range(nb_caches):
            (idd, lc) = [int(k) for k in inF.readline().rstrip().split(' ')]
            #print(inF.readline().rstrip().split(' '))
            dic_caches[idd] = Cache(idd, lc)
        endpoints.append(Endpoint(id_endpoint, latency, dic_caches))
        id_endpoint = id_endpoint+1
    assert(len(endpoints)==E)

    endpoints_dict = {}
    for e in endpoints:
        endpoints_dict[e.id] = e
    # print( [int(k) for k in inF.readline().rstrip().split(' ')])
    requests = []
    for req in range(R):
        (rv, re, rn ) = [int(k) for k in inF.readline().rstrip().split(' ')]
        requests.append(Request(videos_dict[rv], endpoints_dict[re], rn))
    assert(len(requests)==R)
    
    caches = [Cache(id=i, capacity=100) for i in range(C)]

    return Problem(V, E, R, C, X, videos, endpoints, caches, requests)



def main():
    filename = "data/kittens.in"

    parse(filename)

if __name__ == "__main__":
    main()
