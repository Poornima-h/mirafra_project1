"""
encapsulation is binding of data
public ->anyone can access within class and out of class also
private ->it can access only within the function
protected -> it can access within the particaular class
"""
class Animal:
      def voice(self):
          _d="ddsds"  #protected method
          __f="ptivate"
          return f'{_d} {__f} every animal as different voice'



a=Animal()
print(a.voice())


