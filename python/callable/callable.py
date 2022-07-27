class Geek:
    def __call__(self):
        print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

# This proves that class is callable
GeekObject = Geek()
GeekObject()
