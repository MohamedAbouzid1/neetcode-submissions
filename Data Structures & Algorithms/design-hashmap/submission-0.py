class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]
        # hash function to store key and index
        # index = key % 10

    def put(self, key: int, value: int) -> None:
        index = key % 10
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index][i] = (key, value)
                return
        
        self.buckets[index].append((key, value))


    def get(self, key: int) -> int:
        index = key % 10
        for i, pair in enumerate(self.buckets[index]):
            if key == pair[0]:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % 10
        for i, pair in enumerate(self.buckets[index]):
            if key == pair[0]:
                self.buckets[index].remove(pair)
                return
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)