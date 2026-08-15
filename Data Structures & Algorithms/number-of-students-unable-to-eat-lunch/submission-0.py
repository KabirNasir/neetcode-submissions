class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        c = 0
        while(True):
            a = q.popleft()
            if(a == sandwiches[0]):
                sandwiches.pop(0)
                c = 0
            else:
                q.append(a)
                c+=1
            if c == len(q):
                break
        return len(q)

