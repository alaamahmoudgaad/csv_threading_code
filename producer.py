
import threading
import pandas as pd


class Producer(threading.Thread):
    def __init__(self, filename, queue):
        super().__init__()
        self.filename = filename
        self.queue = queue

    def run(self):
        try:
            reader = pd.read_csv(
                self.filename,
                header=None,
                chunksize=50000,
                encoding="latin",
                usecols=[34],
                dtype={34: "string"},
            )

            for chunk in reader:
                self.queue.put(chunk)

        except Exception as error:
            print("Producer error:", error)

        finally:
            self.queue.put(None)
