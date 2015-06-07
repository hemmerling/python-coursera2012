class Overload:
    def __init__(self, value1):
        pass
    def __init__(self, value1, value2):
        pass

my_overload2 = Overload(1,2)
my_overload1 = Overload(1)
