class SuperFizzBuzz():
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi
    
    def __str__(self):
        print("This is SuperFizzBuzz in the range of {} {}". format(self.mini, self.maxi))
    
    def superFizzBuzz(self):
        divide ={'3' : 'Fizz',
                 '7' : 'Buzz',
                 '38' : 'Bazz',
            }
        i = self.mini
        while(i<self.maxi):
            str = ""
            for k in divide.keys():
                if i % int(k) == 0:
                    str += divide[k]
            if str == "":
                print i
            else:
                print str
            i +=1

mini = int(input("Enter the minimum value of the range: "))
maxi = int (input("Enter the maximum value of the range: "))
mini = min(mini, maxi)
maxi = max(mini, maxi)
sol = FizzBuzz(mini,maxi)
sol.__str__()
sol.superFizzBuzz()