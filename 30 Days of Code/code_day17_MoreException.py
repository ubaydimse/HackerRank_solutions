#Write your code here, python 3

#Also, since the method does not reference any class or instance attributes,
#you could make it a static method by using the @staticmethod decorator,
#which provides more flexibility by allowing you to call the method without creating a Calculator instance.

class Calculator:
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n ** p

/* python 3
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')    
        return n ** p
*/

/* python 2
  def power(self,n,p):
    self.n = n
    self.p = p
    if n < 0 or p < 0:
        raise Exception("n and p should be non-negative")
    else:
        return n**p
*/

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
