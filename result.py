from typing import *
from parser import *


class Solution:
    def __init__(self, problem: Problem, assignement: Dict[Cache, List[Video]]):
        self.assignement = assignement
        self.inverse_assignement = {}
        self.compute_inverse()
        self.problem = problem

    def verify_assignement(self):
        for c, vs in self.assignement.items():
            sum_size = sum(v.size for v in vs)
            if sum_size > c.capacity:
                print("NOOOOOOOOOOOOOO  !!!!!!!!!")
                print("At {0} {1}".format(c.id))
                break

    def compute_inverse(self):
        for c, vs in self.assignement.items():
            for v in vs:
                if v not in self.inverse_assignement:
                    self.inverse_assignement[v] = []
                self.inverse_assignement[v].append(c)

    def compute_total_lat(self):
        res = 0
        for req in self.problem.requests:
            v = req.video
            e = req.endpoint
            cs = self.inverse_assignement[v]
            min_latency = min([e.caches_latency[c] for c in cs if c in e.caches_latency.keys()] + [e.dc_latency])
            res += min_latency*req.reqs
        return res
