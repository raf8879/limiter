def limiter(limit, unique, lookup):
    my_sk = {}

    def wrapper(cls):
        def wrapper_2(*args, **kwargs):
            nonlocal limit
            s = cls(*args, **kwargs)
            a = s.__dict__[unique]
            while limit > 0:
                if a not in my_sk:
                    my_sk.setdefault(a, s)
                limit -= 1
                return my_sk[a]
            else:
                if a in my_sk:
                    return my_sk[a]
                return list(my_sk.values())[0] if lookup == 'FIRST' else list(my_sk.values())[-1]
        return wrapper_2
    return wrapper


@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)
obj2 = MyClass(2, 8)
obj3 = MyClass(3, 10)

obj4 = MyClass(4, 0)
obj5 = MyClass(2, 20)

print(obj4.value)
print(obj5.value)