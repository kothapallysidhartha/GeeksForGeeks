#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # Convert the number to a string to iterate over digits
        k = str(n)
        count = 0
        for i in k:
            digit = int(i)
            # Check if the digit is not zero and evenly divides n
            if digit != 0 and n % digit == 0:
                count += 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends