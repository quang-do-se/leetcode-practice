class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        begin = t - 3000

        while self.requests[0] < begin:
            self.requests.pop(0)

        return len(self.requests)


""" pings = [[1], [100], [3001], [3002]] """
pings = [[642],[1849],[4921],[5936],[5957]]
obj = RecentCounter()

for ping in pings:
  if len(ping) > 0:
    print(obj.ping(ping[0]))