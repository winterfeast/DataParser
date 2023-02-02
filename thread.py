from time import sleep
from threading import Thread

def task():
    # block for a moment
    sleep(5)
    # display a message
    print('This is coming from another thread')

thread = Thread(target=task)

thread.start()


print('Waiting for the new thread to finish...')
thread.join()
