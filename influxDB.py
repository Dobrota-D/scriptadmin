import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Initialize client
token = ton token
org = ton organisation
url = ton url

client = influxdb_client.InfluxDBClient(url, token, org)

bucket= ton bucket

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
    .field("percent", usage.percent)
  )
  write_api.write(bucket, org, record)

