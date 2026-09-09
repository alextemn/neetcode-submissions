class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        res = []
        words = text.split(" ")
        syns = {}
        
        def find(x):
            syns.setdefault(x, x)

            if syns[x] != x:
                syns[x] = find(syns[x])

            return syns[x]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                syns[root_a] = root_b
        for a, b in synonyms:
            union(a, b)
        
        groups = {}

        for word in syns:
            root = find(word)
            groups.setdefault(root, []).append(word)
        
        for group in groups.values():
            group.sort()

        def backtrack(i, sen):
            if i == len(words):
                res.append(" ".join(sen))
                return
            word = words[i]

            if word in syns:
                choices = groups[find(word)]
            else:
                choices = [word]

            for choice in choices:
                sen.append(choice)
                backtrack(i + 1, sen)
                sen.pop()

            return
        backtrack(0, [])
        
        return sorted(res)