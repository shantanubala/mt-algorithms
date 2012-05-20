import threading
import random
import time

LIST_SIZE = 200000
TOTAL_ITERATIONS = 20

def merge(left, right):
  result = []

  while left and right:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  if left:
    result.extend(left)
  if right:
    result.extend(right)
  return result

def merge_sort(l):
  if len(l) < 2:
    return l
  middle = len(l) / 2
  left = merge_sort(l[:middle])
  right = merge_sort(l[middle:])
  return merge(left, right)

class ThreadedSort(threading.Thread):
  def __init__(self, lst, **kwargs):
    self.lst = lst
    threading.Thread.__init__(self, **kwargs)

  def run(self):
    l = self.lst
    if 1 < len(l) < 1000:
      middle = len(l) / 2
      left = merge_sort(l[:middle])
      right = merge_sort(l[middle:])
      self.lst = merge(left, right)
    else:
      middle = len(l) / 2
      left_thread = ThreadedSort(l[:middle])
      right_thread = ThreadedSort(l[middle:])
      left_thread.start()
      right_thread.start()
      left_thread.join()
      right_thread.join()
      self.lst = merge(left_thread.lst, right_thread.lst)

total_utime = 0
total_ttime = 0

for y in range(TOTAL_ITERATIONS):
  sample_list = []
  for i in range(LIST_SIZE):
    sample_list.append(random.randint(0, LIST_SIZE))

  start = time.time()
  single_sorted = merge_sort(sample_list)
  utime = time.time() - start
  print "Regular implementation:", utime, "seconds."

  threaded_sample = ThreadedSort(sample_list)
  start = time.time()
  threaded_sample.start()
  threaded_sample.join()
  threaded_sorted = threaded_sample.lst
  ttime = time.time() - start
  print "Threaded implementation:", ttime, "seconds."

  print "Threading overhead: ", ttime - utime, "seconds."

  equal = True
  for x in range(LIST_SIZE):
    if single_sorted[x] != threaded_sorted[x]:
      equal = False
      break

  if equal:
    print "The results are equal."
  else:
    print "Thre results are not equal."

  total_utime += utime
  total_ttime += ttime

print "Unthreaded:Threaded ratio: ", total_utime / total_ttime
