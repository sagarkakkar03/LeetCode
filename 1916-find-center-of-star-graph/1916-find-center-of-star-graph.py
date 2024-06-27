class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph_nodes = set()
        for u, v in edges:
            if u in graph_nodes:
                return u
            if v in graph_nodes:
                return v
            graph_nodes.add(u)
            graph_nodes.add(v)