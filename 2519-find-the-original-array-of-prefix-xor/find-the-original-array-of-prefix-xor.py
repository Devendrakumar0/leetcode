class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        r=[]
        c=pref[0]
        r.append(c)
        for i in range(1, len(pref)):
            r.append(c^pref[i])
            c=pref[i]
        return r


            
        