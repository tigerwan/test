from lib.controller import controller

@controller.register
class worker:
    def __init__(self):
        print("this is worker")

    def run(self):
        print("run worker")

