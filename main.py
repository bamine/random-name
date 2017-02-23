from parser import *

if __name__ == '__main__':
    video_sizes = [50, 50, 80, 30, 110]
    videos = [Video(id=i, size=video_sizes[i]) for i in range(len(video_sizes))]
    caches = [Cache(id=i, capacity=100) for i in range(3)]
    caches_latency_0 = {
        caches[0]: 100,
        caches[1]: 200,
        caches[2]: 200
    }
    endpoint_0 = Endpoint(id=0, dc_latency=1000,
                          caches_latency=caches_latency_0)
    endpoint_1 = Endpoint(id=1, dc_latency=500,
                          caches_latency={})
    endpoints = [
        Endpoint(id=0, dc_latency=1000, caches_latency=caches_latency_0),
        Endpoint(id=1, dc_latency=500, caches_latency={})
        ]
    requests = [
        Request(endpoint=endpoints[0], video=videos[3], reqs=1500),
        Request(endpoint=endpoints[1], video=videos[0], reqs=1000),
        Request(endpoint=endpoints[0], video=videos[4], reqs=500),
        Request(endpoint=endpoints[0], video=videos[1], reqs=1000)
    ]
    problem = Problem(V=5, E=2, R=4, C=3, X=100,
                      videos=[Video],
                      endpoints=endpoints,
                      caches=caches,
                      requests=requests)
