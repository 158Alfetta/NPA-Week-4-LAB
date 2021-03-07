import threading

def print_i(i):
    print(i)

threads = []
for i in range(100):
    thread_arg = [i]
    threads.append(threading.Thread(target=print_i, args=thread_arg))

for t in threads:
    t.start()