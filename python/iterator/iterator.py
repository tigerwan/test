"""
__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
__next__ ( __next__ in Python 3) The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object which further uses next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.
"""
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):

        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x

# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)
