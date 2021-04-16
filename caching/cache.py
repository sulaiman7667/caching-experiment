from memory import Memory

# Your implementations of the classes below should not
# include any additional print statements.


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        global i, cache
        i = 0
        cache = [[None, None], [None, None], [None, None], [None, None]]

    def lookup(self, address):
        global i, cache
        if(i == 4):
            i = 0
        for a in range(4):
            if(cache[a][0] == address):
                return cache[a][1]
        else:
            cache[i][0] = address
            cache[i][1] = super().lookup(address)
            i = i + 1
            return cache[i-1][1]


class LRUCache(Memory):
    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with a cache size of
    # 4. You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        global i, cache
        i = 0
        cache = [[None, None, 0], [None, None, 0],
                 [None, None, 0], [None, None, 0]]

    def lookup(self, address):
        global i, cache
        cache = sorted(cache, key=lambda x: x[2])
        for a in range(4):
            if(address == cache[a][0]):
                cache[a][2] = cache[3][2] + 1
                return cache[a][1]

        else:
            cache = sorted(cache, key=lambda x: x[2])
            cache[0][0] = address
            cache[0][1] = super().lookup(address)
            cache[0][2] = cache[3][2] + 1
            return cache[0][1]
