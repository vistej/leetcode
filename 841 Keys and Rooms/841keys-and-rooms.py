class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can = {0: 1}
        cant = {}

        for i,r in enumerate(rooms):
            if i in can:
                while r:
                    n = []
                    for k in r:
                        if not k in can:
                            can[k] = 1
                            if k in cant:
                                del cant[k]
                            n.extend(rooms[k])
                    r = n
            else:
                cant[i] = 1
        return not len(cant)
