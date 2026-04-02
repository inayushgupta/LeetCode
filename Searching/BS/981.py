class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        values = self.store.get(key, [])
        res = ""

        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            curr_value, curr_time = values[mid]

            if curr_time <= timestamp:
                res = curr_value
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
