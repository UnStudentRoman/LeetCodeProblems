class TimeMap:

    def __init__(self):
        self.keys = {}
        """
        keys: 
            {
                key_1: 
                    {
                        timestamp_1: val_1,
                        timestamp_2: val_2
                    },
                key_2: 
                    {
                        timestamp_1: val_1,
                        timestamp_2: val_2
                    },    
            }
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            if timestamp in self.keys[key]:
                self.keys[key][timestamp] = value
            else:
                self.keys[key] = {timestamp: value}
        else:
            self.keys = {key: {timestamp: value}}

    def get(self, key: str, timestamp: int) -> str:

        while timestamp > 0:
            try:
                return self.keys[key][timestamp]
            except KeyError:
                timestamp -= 1
        return ""



if __name__ == '__main__':
    operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    values = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    for operation, value in zip(operations,values):
        if operation == "TimeMap":
            obj = TimeMap()

        elif operation == "set":
            obj.set(key=value[0], value=value[1], timestamp=value[2])

        elif operation == "get":
            print(obj.get(key=value[0], timestamp=value[1]))