import psutil
import argparse
import time

from influxDB import *

def get_interval():
  """
  Get the interval before two metrics pull
  
  :return: interval
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--interval", help="Nombre de secondes d'intervalle", type=int, required=True)
  args = parser.parse_args()
  
  return args.interval


def get_cpu_metrics(interval):
  """
  Get and send CPU metrics
  
  :param interval: interval between two metrics pulling
  """
  percent_of_use = psutil.cpu_percent(interval)
  percent_of_use_per_cpu = psutil.cpu_percent(interval, percpu=True)
  count = psutil.cpu_count()
  count_physical = psutil.cpu_count(logical=False)

  send_cpu_metrics(percent_of_use, percent_of_use_per_cpu, count, count_physical)
    
def get_storage_disk_metrics():
  """
  Get and send disk storage metrics
  
  :param interval: interval between two metrics pulling
  """
  usage = psutil.disk_usage('/')
  
  send_disk_storage_metrics(usage)
    

interval = get_interval()

# Infinity loop who send every metrics at the interval set by user
while True:
  get_cpu_metrics(interval)
  get_storage_disk_metrics()

  time.sleep(interval)

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
