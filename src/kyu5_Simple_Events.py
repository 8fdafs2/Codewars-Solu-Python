class Solution():
    """
    Your goal is to write an Event constructor function,
    which can be used to make event objects.

    An event object should work like this:

        it has a .subscribe() method,
            which takes a function and stores it as its handler
        it has an .unsubscribe() method,
            which takes a function and removes it from its handlers
        it has an .emit() method,
            which takes an arbitrary number of arguments and calls all the stored functions with these arguments

    As this is an elementary example of events, there are some simplifications:

        all functions are called with correct arguments (e.g. only functions will be passed to unsubscribe)
        you should not worry about the order of handlers' execution
        the handlers will not attempt to modify an event object (e.g. add or remove handlers)
        the context of handlers' execution is not important
        each handler will be subscribed at most once at any given moment of time. It can still be unsubscribed and then subscribed again

    Also see an example test fixture for suggested usage

    """
    def __init__(self):
        pass

    class Event_01():

        def __init__(self):
            self.hashtab = {}

        def subscribe(self, func):
            self.hashtab[func] = 1

        def unsubscribe(self, func):
            del self.hashtab[func]

        def emit(self, *args, **kwargs):
            for func in self.hashtab:
                func(*args, **kwargs)


    class Event_02():
        def __init__(self):
            self.hashtab = set()

        def subscribe(self, func):
            self.hashtab.add(func)

        def unsubscribe(self, func):
            self.hashtab.remove(func)

        def emit(self, *args, **kwargs):
            for func in self.hashtab:
                func(*args, **kwargs)