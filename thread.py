import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 100:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

def f(a,d):
   for i in range(100):
      time.sleep(d)
      print a

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   thread.start_new_thread( print_time, ("Thread-2", 5, ) )
   thread.start_new_thread( f, ('kathir', 10))
   thread.start_new_thread( f, ('raja', 4))
except:
   print "Error: unable to start thread"


