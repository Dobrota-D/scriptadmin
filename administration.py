from tracemalloc import get_traced_memory
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
  """
  usage = psutil.disk_usage('/')
  
  send_disk_storage_metrics(usage)
    
def get_sensor_metrics():
  """
  Get and send sensor metrics
  """  
  temperatures = psutil.sensors_battery()
  send_sensors_metrics(temperatures)
    
def get_network_metrics():
  """
  Get and send network metrics
  """
  network = psutil.net_io_counters()
  send_networks_metrics(network)
    
def get_memory_metrics():
  """
  Get and send memory metrics
  """
  virtual = psutil.virtual_memory()
  swap = psutil.swap_memory()
  
  send_memory_metrics(virtual, swap)
    

interval = get_interval()

# Infinity loop who send every metrics at the interval set by user
while True:
  get_cpu_metrics(interval)
  get_storage_disk_metrics()
  get_sensor_metrics()
  get_network_metrics()
  get_memory_metrics()
  
  time.sleep(interval)
