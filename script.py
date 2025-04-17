def is_divisible(func):
    def inner(x, y):
        if y == 0:
            raise ValueError(f"divider can not be 0, got {y}")
        else:
            return True
    return inner
        
@is_divisible
def divide_it(x, y):
    return x/y

divide_it(10, 1)