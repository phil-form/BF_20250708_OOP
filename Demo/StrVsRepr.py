class Test:
    def __str__(self):
        return "STR TEST"

    def __repr__(self):
        return "REP TEST"

class Test2:
    def __init__(self):
        self.test = Test()


test = Test()
# STR
print(test)
# STR
print(f"{test}")
# forcer le repr
print(repr(test))
# REPR
print(Test2().__dict__)
