class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a = 0
        b = 0
        for s in students:
            if s:
                a +=  1
            else:
                b += 1
        for s in sandwiches:
            if s:
                if a == 0:
                    return b
                a -= 1
            else:
                if b == 0:
                    return a
                b -= 1
        return a + b