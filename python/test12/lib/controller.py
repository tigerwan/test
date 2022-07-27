
class controller:
    workers = {}
    def __init__(self):
        pass
    @classmethod
    def register(cls, control_cls):
        print("register worker:", control_cls.__name__)
        cls.workers[control_cls.__name__] = control_cls
        return control_cls

    @classmethod
    def get_workers(cls):
        return cls.workers

    def run(self):
        print("workers:", self.workers)
        for key, worker_cls in self.workers.items():
           worker_cls().run()


