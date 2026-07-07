class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mat = []
        for i in range(len(position)):
            mat.append([position[i],speed[i]])
        mat.sort(reverse=True)
        print(mat)
        
        stack = []
        for j in range(len(mat)):
            i = mat[j]
            time =  (target - i[0])/ i[1]
            if stack and time<=stack[-1]:
                continue
            else:
                stack.append(time)

        print(stack)

        return len(stack)