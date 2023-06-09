class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # set to keep track of visited numbers
        
        while n != 1:  # continue loop until happy or stuck in cycle
            sum_of_squares = 0
            
           
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            
            
            if sum_of_squares in visited:
                return False
            
            visited.add(sum_of_squares)
            
            n = sum_of_squares
        
        return True
