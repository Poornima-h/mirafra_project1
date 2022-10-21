from abc import ABC,abstractmethod
class myclass:
    def voice(self):
       pass

class child1(myclass):
    def voice(self):
        super().voice()
        return 'cat voice'

class child2(myclass):
    def voice(self):
        return 'dog voice'
obj=child2()
print(obj.voice())

obj2=child1()
print(obj2.voice())

from abc import ABC,abstractmethod
class myclass:
    @abstractmethod
    def voice(self):
       pass

class child1(myclass):
    def voice(self):
        super().voice()
        return 'cat voice'

class child2(myclass):
    def voice(self):
        return 'dog voice'
obj=child2()
print(obj.voice())

obj2=child1()
print(obj2.voice())
