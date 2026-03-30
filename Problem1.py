# Beautiful Arrangement
# Time Complexity -> O(K) where k < N! since at every step we have 1 less option to add and the validate skips 
# unwanted recrusion possibles compleetly, so it will never be N!
# Space Complexity -> O(N) stack space and the visitedNumbers array
# Logic -> logically adding the number in a vertual list using recursion, and before adding the number validatig the contraint of beautiful num
# Once all elements in a perm is added increase the result
class Solution:
    def countArrangement(self, n: int) -> int:
        
        result = 0
        visitedNumbers = [False]*(n+1)
        # perm = []


        def validate(number, position):
            if position%number == 0 or number%position == 0:
                return True
            return False

        def helper(position):
            nonlocal result
            if position == 0:
                result+=1
                return

            for i in range(n):
                if not visitedNumbers[i+1] and validate(position, i+1):
                    # perm.append(i+1)
                    visitedNumbers[i+1] = True
                    helper(position-1)
                    # item = perm.pop()
                    visitedNumbers[i+1] = False
        helper(n)
        return result