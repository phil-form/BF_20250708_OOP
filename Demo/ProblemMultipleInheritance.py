class Parent1:
    def function(self):
        print("Parent 1")

class Parent2:
    def function(self):
        print("Parent 2")

class Child1(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

    def function(self):
        super().function()
        Parent2.function(self)


child = Child1()
child.function()