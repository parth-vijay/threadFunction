# System modules
from Queue import Queue
from threading import Thread
import time

concurrent = 5
que = Queue(concurrent*1)

def DataProcess():
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    while True:
        function process......

        q.task_done()


# Set up some threads to fetch the enclosures
for i in range(concurrent):
	t = Thread(target=DataProcess)
	t.daemon = True
	t.start()

for user in userList:
    que.put(user)

que.join()
