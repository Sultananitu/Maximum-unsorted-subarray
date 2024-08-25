class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
         B = sorted()
        start = -1
        for i in range(len(A)):
            if A[i] != B[i]:
                start = i
                break
                
        if start == -1:
            return [-1]
        end = -1
        for i in range(len(A)-1, -1, -1):
            if A[i] != B[i]:
                end = i
                break
                
        return [start, end]