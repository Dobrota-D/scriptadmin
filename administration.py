import argparse
import logging
import psutil
import time
from influxDB import *


def get_log_level():
  """
  Get the log level from args
  :return: log level
  """

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
    
# Argparse initialization
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interval", help="Nombre de secondes d'intervalle", type=int, required=True)
parser.add_argument("-l", "--logging", help="Niveau de logging", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='CRITICAL')
args = parser.parse_args()

# Logging initialization
logging.basicConfig(
  format='%(asctime)s [%(levelname)s]: %(message)s',
  datefmt='%d-%m-%Y:%H:%M:%S',
  filename='administration.log',
  encoding='utf-8',
  level=args.logging
)

logging.info('Script starting...')
logging.info(f'Interval = {args.interval}s')


# Infinity loop who send every metrics at the interval set by user
loop_nb = 0
while True:
  logging.info(f'Starting the loop {loop_nb}')
  loop_nb += 1
  
  # Call all metrics pulling functions
  get_cpu_metrics(args.interval)
  get_storage_disk_metrics()
  get_sensor_metrics()
  get_network_metrics()
  get_memory_metrics()
  
  time.sleep(args.interval)
