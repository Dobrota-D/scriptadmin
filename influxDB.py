import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

# Initialize client
token = os.getenv('TOKEN_API')
org = os.getenv('ORGANISATION_NAME')
url = os.getenv('URL_DB')

client = influxdb_client.InfluxDBClient(url, token, org)
bucket= os.getenv('BUCKET_NAME')

write_api = client.write_api(write_options=SYNCHRONOUS)


def send_cpu_metrics(percent_of_use, percent_of_use_per_cpu, count, count_physical):
  """
  Send CPU metrics into the Influx database
  :param percent_of_use: the percentage of cpu usage
  :param percent_of_use_per_cpu: the percentage of cpu each usage
  :param count: the number of cpu
  :param count_physical:  the number of physical cpu
  """
  record = (
    Point("measurement1")
    .tag("tag", "cpu")
    .field("percent_of_use", percent_of_use)
    .field("percent_of_use_0", percent_of_use_per_cpu[0])
    .field("percent_of_use_1", percent_of_use_per_cpu[1])
    .field("percent_of_use_2", percent_of_use_per_cpu[2])
    .field("percent_of_use_3", percent_of_use_per_cpu[3])
    .field("percent_of_use_4", percent_of_use_per_cpu[4])
    .field("percent_of_use_5", percent_of_use_per_cpu[5])
    .field("percent_of_use_6", percent_of_use_per_cpu[6])
    .field("percent_of_use_7", percent_of_use_per_cpu[7])
    .field("count", count)
    .field("count_physical", count_physical)
    
  )
  write_api.write(bucket, org, record)


def send_disk_storage_metrics(usage):
  """
  Send disk storage metrics into the Influx database
  :param usage: disk usage statistics
  """
  record = (
    Point("measurement1")
    .tag("tag", "disk_storage")
    .field("total", usage.total)
    .field("used", usage.used)
    .field("free", usage.free)
    .field("percent", int(usage.percent))
  )
  write_api.write(bucket, org, record)

def send_sensors_metrics(battery):
  """
  Send sensors metrics into the Influx database
  :param battery: battery sensors statistics
  """
  record = (
    Point("measurement1")
    .tag("tag", "sensors")
    .field("percent", int(battery.percent))
    #.field("secsleft", battery.secsleft)
    #.field("power_plugged", battery.power_plugged)
  )
  write_api.write(bucket, org, record)
  
def send_networks_metrics(network):
  """
  Send networks metrics into the Influx database
  :param network: network statistics
  """
  record = (
    Point("measurement1")
    .tag("tag", "network")
    .field("bytes_sent", network.bytes_sent)
    .field("bytes_recv", network.bytes_recv)
    .field("packets_sent", network.packets_sent)
    .field("packets_recv", network.packets_recv)
  )
  write_api.write(bucket, org, record)
  
def send_memory_metrics(virtual, swap):
  """
  Send memory metrics into the Influx database
  :virtual: virtual memory statistics
  :swap: swap memory statistics
  """
  record = (
    Point("measurement1")
    .tag("tag", "memory")
    .field("virtual_total", virtual.total)
    .field("virtual_available", virtual.available)
    .field("virtual_percent", virtual.percent)
    .field("virtual_used", virtual.used)
    .field("virtual_free", virtual.free)
    .field("virtual_active", virtual.active)
    .field("virtual_inactive", virtual.inactive)
    .field("virtual_wired", virtual.wired)
    .field("swap_total", swap.total)
    .field("swap_used", swap.used)
    .field("swap_free", swap.free)
    .field("swap_percent", swap.percent)
    .field("swap_sin", swap.sin)
    .field("swap_sout", swap.sout)
  )
  write_api.write(bucket, org, record)