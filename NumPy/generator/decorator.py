def decore(fun):
    def inner(name):
        print("hello world")
        fun(name)
    return inner
@decore
def wish(name):
    print("hello space")
wish('a')