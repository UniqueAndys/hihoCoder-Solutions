n = int(raw_input())

'''
class Node():
    def __init__(self):
        self.d = {}
'''

class Trie():
    def __init__(self):
        self.head = {}

    def add(self, s):
        p = self.head
        for c in s:
            if c not in p:
                p[c] = [{}, 0]
            p[c][1] += 1
            p = p[c][0]

    def search(self, s):
        p = self.head
        for c in s[:-1]:
            if c not in p:
                return 0
            p = p[c][0]
        if s[-1] not in p:
            return 0
        else:
            return p[s[-1]][1]

trie = Trie()

for i in xrange(n):
    s = raw_input()
    trie.add(s)

m = int(raw_input())
for i in xrange(m):
    s = raw_input()
    print trie.search(s)
