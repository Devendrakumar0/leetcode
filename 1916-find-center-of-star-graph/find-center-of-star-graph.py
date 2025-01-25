class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if len(edges) < 2:
            return 0  
        firstedge = edges[0]
        secondedge = edges[1]
        star = set(firstedge) & set(secondedge)
        return star.pop()
        