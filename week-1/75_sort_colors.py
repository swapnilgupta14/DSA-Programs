def Sort(A):
        freq=[0]*r
        for i in A:
            freq[i]=freq[i]+1
        k=0
        for i in range(r):
            while(freq[i]>0):
                A[k]=i
                freq[i]=freq[i]-1
                k+=1
r=3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        Sort(nums)
        return nums
