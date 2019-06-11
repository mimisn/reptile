from multiprocessing import Process


class GetUrlProcess(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue
        self.daemon = True

    def run(self):
        pass