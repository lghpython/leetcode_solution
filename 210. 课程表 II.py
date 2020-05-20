def findOrder(numCourses, prerequisites):
    visited = [0] * numCourses
    res = []
    # 保存依赖关系到字典
    condiction = [[] for _ in range(numCourses)]
    for cur, pre in prerequisites:
        condiction[cur].append(pre)

    def dsf(i):
        if visited[i] != 0:
            return visited[i]
        visited[i] = False
        for j in condiction[i]:
            if not dsf(j):
                return False
        visited[i] = True
        res.append(i)
        return True

    # 遍历有先觉条件的课程
    for i in range(numCourses):
        if not dsf(i):
            return []
    print(res)
    return res


if __name__ == '__main__':
    findOrder(3,[[0,1],[0,2],[1,2]])
    findOrder(2, [[0,1]])
    findOrder(2, [])


