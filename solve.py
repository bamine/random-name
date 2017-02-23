from typing import *
from result import *
from itertools import *
from operator import *
from pulp import *


def solve1(problem: Problem):
    #for each endpoint sort videos by nb requests
    #for each enpoints sort caches by latency
    #for each endpoint and each cache
    #fill cache with videos until cache is full
    sol = {}
    assigned = {}
    for e in problem.endpoints:
        requests = [req for req in problem.requests if req.endpoint.id == e.id]
        video_reqs = [(req.video, -req.reqs) for req in requests]
        video_reqs_grouped = {}
        for v, r in video_reqs:
            if v in video_reqs_grouped:
                video_reqs_grouped[v] += r
            else:
                video_reqs_grouped[v] = r
        sorted_videos = sorted(video_reqs_grouped.items(), key=itemgetter(1), reverse=True)
        sorted_caches = sorted(e.caches_latency.keys(), key=lambda c: e.caches_latency[c])
        cache_counter = 0
        video_counter = 0
        while cache_counter < len(sorted_caches) and video_counter < len(sorted_videos):
            #print("Endpoint {0} cache {1}".format(e.id, cache_counter))
            cache = sorted_caches[cache_counter]
            #print("cache capacity ", cache.current_capacity)
            video = sorted_videos[video_counter][0]
            if video.id not in assigned.get(cache.id, set()) and (sum(v.size for v in sol.get(cache, [])) + video.size) <= cache.capacity:
                if cache in sol:
                    sol[cache].append(video)
                    assigned[cache.id].add(video.id)
                else:
                    sol[cache] = [video]
                    assigned[cache.id] = {video.id}
                cache.current_capacity += video.size
                video_counter += 1
            else:
                cache_counter += 1
    return sol


def solve2(problem: Problem):
    prob = LpProblem("hashcode", LpMinimize)
    x = LpVariable.dicts("x", [
        (i, j) for i in range(len(problem.videos)) for j in range(len(problem.caches))
        ], 0, 1, LpBinary)
    for j, cache in enumerate(problem.caches):
        prob += lpSum(x[(i, j)]*v.size for i, v in enumerate(problem.videos)) <= cache.capacity
    for r, request in enumerate(problem.requests):
        min(x[(request.video.id, c)]*request.endpoint.caches_latency[c] for c in problem.caches)





