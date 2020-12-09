import os
class Log():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if not os.path.exists("log"):
            os.makedirs("log")
        with open("{}/log/{}.log".format(os.getcwd(),args[0].nev),mode="a+", encoding="utf-8") as file:
            file.write("{}\n".format(self.func.__name__))
        return self.func(*args, **kwargs)


