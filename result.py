from typing import *
from parser import *


class Solution:
    def __init__(self, problem: Problem, assignment: Dict[Cache, List[Video]]):
        self.assignment = assignment
        self.inverse_assignment = {}
        self.compute_inverse()
        self.problem = problem

    def verify_assignement(self):
        for c, vs in self.assignment.items():
            sum_size = sum(v.size for v in vs)
            if sum_size > c.capacity:
                print("NOOOOOOOOOOOOOO  !!!!!!!!!")
                print("At {0} {1}".format(c.id))
                break

    def compute_inverse(self):
        for c, vs in self.assignment.items():
            for v in vs:
                if v not in self.inverse_assignment:
                    self.inverse_assignment[v] = []
                self.inverse_assignment[v].append(c)

    def compute_total_lat(self):
        res = 0
        for req in self.problem.requests:
            v = req.video
            e = req.endpoint
            cs = self.inverse_assignment.get(v, [])
            min_latency = min([e.caches_latency[c] for c in cs if c in e.caches_latency.keys()] + [e.dc_latency])
            res += (e.dc_latency - min_latency)*req.reqs
        return res

    def submission(self):
        submission_str = "{n_caches}".format(n_caches=len(self.assignment))
        for c in self.assignment:
            submission_str += str(c.id)
            values = [str(c.id)] + [str(v.id) for v in self.assignment[c]]
            submission_str += '\n' + ' '.join(values)
        return submission_str
