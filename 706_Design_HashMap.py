from hashlib import sha256


class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        hash_val = sha256(str(key).encode()).hexdigest()
        if self.get(key) != -1:
            for item in self.hashmap:
                if item[0] == hash_val:
                    item[1] = (key, value)
                    return None
        self.hashmap.append([hash_val, (key, value)])
        return None

    def get(self, key: int) -> int:
        hash_val = sha256(str(key).encode()).hexdigest()
        try:
            for item in self.hashmap:
                if item[0] == hash_val:
                    return item[1][1]
            else:
                return -1
        except ValueError:
            return -1

    def remove(self, key: int) -> None:
        hash_val = sha256(str(key).encode()).hexdigest()
        try:
            for item in self.hashmap:
                if item[0] == hash_val:
                    self.hashmap.pop(self.hashmap.index(item))
            # self.hashmap.pop(self.hashmap.index(hash_val))
        except ValueError:
            return None
        return None


if __name__ == '__main__':
    methods = ["MyHashMap","put","put","get","get","put","get","remove","get"]
    values = [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
    obj = None
    # Your MyHashMap object will be instantiated and called as such:
    for method, value in zip(methods, values):
        # print(i, j)
        if method == "MyHashMap":
            obj = MyHashMap()
        elif method == "put":
            obj.put(value[0], value[1])
        elif method == "get":
            print(obj.get(value[0]))
        elif method == "remove":
            obj.remove(value[0])

