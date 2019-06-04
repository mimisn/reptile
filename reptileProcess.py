from multiprocessing import Process


class GetUrlProcess(Process):
    def __init__(self, queue, mutex):
        Process.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.daemon = True

    def run(self):
        pass