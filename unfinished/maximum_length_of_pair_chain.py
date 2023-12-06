class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs = sorted(pairs)
        counter = 0
        for pair in pairs:
            previous = pairs[pairs.index(pair) - 1]
            if previous[-1] == pair[0] or previous[0] == pair[0]:
                pairs.remove(pair)
        # print(pairs)
        for pair in pairs:
            # print(pair)
            try:
                previous = pairs[pairs.index(pair) - 1]
                # print(previous)
                if previous == pairs[-1]:
                    raise(IndexError)
                if pair[0] > previous[-1]:
                    counter += 1
            except IndexError: # to deal with first entry 
                # print("hi")
                counter += 1

        return(counter)
    
print(Solution().findLongestChain([[1,2],[7,8],[4,5]]))
    
