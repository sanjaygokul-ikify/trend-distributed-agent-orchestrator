import time

class Metrics:
  def __init__(self):
    self.start_time = time.time()

  def elapsed_time(self) -> int:
    return int(time.time() - self.start_time)

  def init_metrics(self):
    return self