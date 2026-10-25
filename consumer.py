
import threading


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        total_found = 0
        total_rows = 0

        while True:
            chunk = self.queue.get()

            try:
                if chunk is None:
                    break

                phones = chunk.iloc[:, 0].astype("string")
                matching = phones.str.startswith("805", na=False)

                total_found += int(matching.sum())
                total_rows += len(chunk)

            finally:
                self.queue.task_done()

        print("Total matching rows:", total_found)
        print("Total rows processed:", total_rows)
