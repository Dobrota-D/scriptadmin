import psutil
import argparse

def get_interval():
  """
  Get the interval before two metrics pull
  
  :return: interval
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--interval", help="Nombre de secondes d'intervalle", type=int, required=True)
  args = parser.parse_args()
  
  return args.interval

def watch_cpu_metrics(interval):
  """
  Watch for cpu metrics 
  
  :param interval: interval between two metrics pull
  """
  # Get percentage of cpu usage fro each cpu
  print('CPU usage for each CPU (%)')
  for x in range(3):
    print(psutil.cpu_percent(interval, percpu=True))

  # Get CPU count
  print('\nCPU count:', psutil.cpu_count())
  print('CPU count (physical)', psutil.cpu_count(logical=False))




interval = get_interval()
print('Interval:', str(interval) + 's\n')

watch_cpu_metrics(interval)