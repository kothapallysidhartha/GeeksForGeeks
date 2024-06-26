#User function Template for python3
class Solution:
    def print2largest(self, arr, n):
        if n < 2:
            return -1  # If there are fewer than 2 elements, there's no second largest

        m = arr[0]
        so = None
        
        for i in range(1, n):
            if arr[i] > m:
                so = m
                m = arr[i]
            elif arr[i] < m and (so is None or arr[i] > so):
                so = arr[i]
        
        return so if so is not None else -1
	            
		        

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends