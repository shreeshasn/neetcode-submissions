class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.q = deque()
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        k = self.q.remove(key)
        self.q.append(key)
        return self.d.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            k = self.q.remove(key)
            self.q.append(key)
        else:
            if len(self.d) < self.c:
                self.d[key] = value
                self.q.append(key)
            else:
                k = self.q.popleft()
                v = self.d.pop(k)
                self.d[key] = value
                self.q.append(key)



