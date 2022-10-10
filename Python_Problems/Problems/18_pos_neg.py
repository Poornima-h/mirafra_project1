#check the number is positive or negative

class myclass:
      def __init__(self,n):
          self.n=n

      @staticmethod
      def welcome():
          return "welcome to my class"

      def check_pos(self,n):
          num = str(n)
          if num[0]=='-':
              return f"{n} is a negative number"
          else:
              return f"{n} is a positive number"

myobj=myclass(10)
print(myobj.welcome())
print(myobj.check_pos(-30))