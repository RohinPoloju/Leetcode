class FizzBuzz(object):
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi 
    
    def __str__(self):
        return("Printing FizzBuzz for the range {} to {}".format(self.mini, self.maxi))   
    
    def fizzbuzz(self):
        i = self.mini
        while (i < self.maxi):
            str1 = ""
            divisible_by_three = (i %3 == 0)
            divisible_by_five = (i %5 == 0)
            if divisible_by_three and divisible_by_five:
                print("FizzBuzz")
            elif divisible_by_five:
                print("Buzz")
            elif divisible_by_three:
                print("Fizz")
            else:
                print(i)
            i += 1
'''
mini = int(input("Enter the minimum value of the range: "))
maxi = int (input("Enter the maximum value of the range: "))
mini = min(mini, maxi)
maxi = max(mini, maxi)
sol = FizzBuzz(mini,maxi)
print(sol)
sol.fizzbuzz()
'''