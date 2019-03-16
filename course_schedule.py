class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0]*numCourses
        courses = {}
        for pair in prerequisites:
            indegree[pair[0]] += 1 
            if pair[1] in courses:
                courses[pair[1]].append(pair[0])
            else:
                courses[pair[1]] = [pair[0]]
        queue = [idx for idx in range(numCourses) if indegree[idx] == 0]
        result = 0
        while queue:
            course = queue.pop(0)
            result += 1
            for c in courses[course]:
                indegree[c] -= 1 
                if indegree[c] == 0:
                    queue.append(c)
        if result == numCourses:
            return True 
        else:
            return False

pairs = [[1,0],[1,2],[0,1]]
s = Solution()
print s.canFinish(3, pairs)
