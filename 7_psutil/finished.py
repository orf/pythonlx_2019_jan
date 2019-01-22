import psutil

for process in psutil.process_iter():
    try:
        print(process.name(), process.memory_percent())
    except psutil.Error:
        pass


for partition in psutil.disk_partitions():
    print(psutil.disk_usage(partition.mountpoint))


print(psutil.sensors_battery())
