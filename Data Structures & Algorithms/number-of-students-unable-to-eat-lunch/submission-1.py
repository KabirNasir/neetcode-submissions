class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)  
        print(cnt)
        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1      
            else:
                break                    
        return cnt[0] + cnt[1]
        
