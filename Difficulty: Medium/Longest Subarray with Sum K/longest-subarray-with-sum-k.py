# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        prefix_map = {}  # Stores {prefix_sum: index}
        max_len = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]  # Compute running sum

            # If sum itself equals k, update max_len
            if prefix_sum == k:
                max_len = i + 1

            # If (prefix_sum - k) exists in the map, update max_len
            if (prefix_sum - k) in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])

            # Store first occurrence of prefix_sum
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_len


        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends