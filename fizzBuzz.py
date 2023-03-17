class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num=[]
        for number in range(1,n+1):
            if number%3==0 and number%5==0:
                num.append("FizzBuzz")
            elif number%3==0:
                num.append("Fizz")
            elif number%5==0:
                num.append("Buzz")
            else:
                num.append(str(number))
        return num


