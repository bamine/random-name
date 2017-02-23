from typing import *
from parser import *


class Solution:
    def __init__(self, problem: Problem, assignement: Dict[Cache, List[Video]]):
        self.assignement = assignement
        self.inverse_ass = {}
        self.problem = problem

    def compute_total_lat(self):
        res = 0
        for req in self.problem.requests:
            v = req.video
            e = req.endpoint
            cs = self.inverse_ass[v]
            min_latency = min([e.caches_latency[c] for c in cs if c in e.caches_latency.keys()] + [e.dc_latency])
            res += min_latency*req.reqs
        return res
