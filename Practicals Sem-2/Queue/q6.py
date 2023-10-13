from queue import Queue


class Printer:
    def __init__(self):
        self.current_job = None

    def print_job(self, job):
        print(f"Printing {job}")


class PrintSpooler:
    def __init__(self):
        self.print_queue = Queue()
        self.printer = Printer()

    def add_job(self, job):
        self.print_queue.put(job)

    def spool_jobs(self):
        while not self.print_queue.empty():
            next_job = self.print_queue.get()
            self.printer.print_job(next_job)


if __name__ == '__main__':
    spooler = PrintSpooler()
    spooler.add_job('Document 1')
    spooler.add_job('Document 2')
    spooler.add_job('Document 3')

    spooler.spool_jobs()
