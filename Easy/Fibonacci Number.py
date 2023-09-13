class Solution:
    def fib(self, n: int) -> int:
        
        arr = [1] * n

        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n-1] if n > 0 else 0