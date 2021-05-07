from django.shortcuts import render
from django.http import HttpResponse
import psutil
import time
from time import localtime, strftime
import json
import asyncio
import websockets
import server

def get_cpu_reading():
	cpu = {} #we will store the cpu readings here
	cpu_readings = psutil.cpu_percent(interval=1, percpu=True)

	#{"cpu0": 52.5, "cpu1": 33.0, "cpu2": 54.5, "cpu3": 35.0}
	for i in range(0,len(cpu_readings)):
		cpu['cpu'+str(i)] = cpu_readings[i]

	return cpu

def get_load_averages():
	load_avg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
	mapped_avg = {"one_min":load_avg[0], "five_min":load_avg[1], "fifteen_min":load_avg[2]}
	return mapped_avg

def get_memory():
	mem = psutil.virtual_memory()
	return mem[2]

def get_disk():
	disk = psutil.disk_usage('/')
	return disk[3]

def get_signal_strength():
	net = psutil.net_io_counters()
	signal = {'Bytes_send':net[0],'Bytes_recv':net[1]}
	return signal

def get_network_traffic():
	net = psutil.net_io_counters()
	traffic = {'Packets_send':net[2],'Packets_recv':net[3]}
	return traffic

async def hello():
    #name = await websocket.recv()
    time.sleep(1)#sleep for 1 second
    reading_time = strftime("%H:%M:%S", localtime())
    send_obj = json.dumps({"time":reading_time,\
    					   "cpu":get_cpu_reading(),\
    					   "load_avg":get_load_averages(),\
    					   "virtual_memory_utilized":get_memory(),\
    					   "disk_utilized":get_disk(),\
						   "signal":get_signal_strength(),\
						   "traffic":get_network_traffic()\
    					   })
    await send_obj
    return send_obj
p = hello()
print(p["cpu"])