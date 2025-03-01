import time


def download():
    print("Starting download...")
    time.sleep(3)  # Simulating an I/O-bound task (e.g., API call)
    print("Download complete.")


start = time.time()
download()
download()
end = time.time()

print("Total time:", end - start)
