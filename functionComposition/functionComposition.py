def compose(f,  g):
    return lambda *args, **kwargs: f(g(*args,**kwargs))

def increment(x):
    return x + 1

def square(x):
    return x ** 2

composed = compose(increment, square)

print composed(5)