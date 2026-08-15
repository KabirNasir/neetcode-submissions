class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)
        c = 0
        while(True):
            a = q.popleft()
            if(a == s[0]):
                s.popleft()
                c = 0
            else:
                q.append(a)
                c+=1
            if c == len(q):
                break
        return len(q)
        
