import collections

class Solution:
    
    def frequencySort(self, s: str) -> str:
        dict = collections.Counter(s)
        ans = ''
        for c in sorted(dict, key=lambda item: dict[item], reverse=True):
            ans+=c*dict[c]
        return ans

if __name__== "__main__" :

    # set test cases
    
    test1 = ["tree","eetr"]
    test2 = ["cccaaa", "aaaccc"]
    test3 = ["Aabb","bbAa"]
    
    tests = [test1, test2, test3]
    # instantiate class
    tree = Solution

    for i in tests:
        print(i[1], tree.frequencySort(tree,s=i[0]), i[1] == tree.frequencySort(tree,s=i[0]))
