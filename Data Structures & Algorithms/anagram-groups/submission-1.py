class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        endThing = []
        #temporary dict
        d = {}
        #list of dictionaries to compare to
        d2 = []
        for stri in strs:
            #assemble the dict
            d.clear()
            for char in stri:
                d[char] = d.get(char, 0) + 1
            for i, dicti in enumerate(d2):
                if dicti == d:
                    endThing[i].append(stri)
                    break
                else:
                    continue
            else:
                d2.append(d.copy());
                endThing.append([stri])
        return endThing

                

            
