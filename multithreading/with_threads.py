import threading
import time


def download():
    print("Starting download...")
    time.sleep(3)  # Simulating an I/O-bound task
    print("Download complete.")


start = time.time()
t1 = threading.Thread(target=download)
t2 = threading.Thread(target=download)

t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()

print("Total time:", end - start)
