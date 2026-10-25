
import queue
from producer import Producer
from consumer import Consumer


def main():
    file_path = "/content/extracted/2.csv"

    data_queue = queue.Queue(maxsize=10)

    producer = Producer(file_path, data_queue)
    consumer = Consumer(data_queue)

    consumer.start()
    producer.start()

    producer.join()
    data_queue.join()
    consumer.join()

    print("All threads finished!")


if __name__ == "__main__":
    main()
