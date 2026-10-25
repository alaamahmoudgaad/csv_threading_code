
import threading
import pandas as pd


class Producer(threading.Thread):
    def __init__(self, file_path, queue, chunk_size=100000):
        super().__init__()
        self.file_path = file_path
        self.queue = queue
        self.chunk_size = chunk_size

    def run(self):
        try:
            for chunk in pd.read_csv(
                self.file_path,
                chunksize=self.chunk_size,
                header=None,
                dtype=str
            ):
                self.queue.put(chunk)

        except Exception as e:
            print("Error reading CSV file:", e)

        finally:
            self.queue.put(None)
