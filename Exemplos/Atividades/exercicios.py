def decor(func):
    def wrap():
        print("-" * 10)
        func()
        print("-" * 10)
    return wrap

@decor
def frase():
    print("Ola")

frase()