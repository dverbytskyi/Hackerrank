# Write your code here

class Calculator():
    @staticmethod  # it is not necessary to create a class instance, so we can just call a class method
    def power(n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return pow(n, p)

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)