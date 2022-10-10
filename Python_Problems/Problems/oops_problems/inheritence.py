#single inheritence
class parent:
      def __str__(self):
          return f'Iam your parent'

class child(parent):
      def __str__(self):
          a=parent.__str__(self)
          b=super().__str__()
          return f'{a} and {b} and IAm your child'
single=child()
print(single.__str__())


#multilevel inheritence
class grandparent:
      def __str__(self):
          return f"iam grand parent"

class parents(grandparent):
      def __str__(self):
          return f'iam father'
class son(parent):
    def __str__(self):
        g=grandparent.__str__(self)
        p=parents.__str__(self)
        return f'{g},{p} and iam your son'
ml=son()
print(ml.__str__())


#multiple inheritence
class father:
    def __str__(self):
        return f"iam mother"

class mother(grandparent):
    def __str__(self):
        return f'iam father'


class daughter(father,mother):
    def __str__(self):
        g = father.__str__(self)
        p = mother.__str__(self)
        return f'{g},{p} and iam your son'


ml2 = daughter()
print(ml2.__str__())
