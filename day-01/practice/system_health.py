import psutil
#take Cpu threshold
def system_health():
    
    cpu_threshold = int(input("ENTTER THE CPU THRESHOLD "))
    disk_threshold = int(input("ENTER THE DISK THRESHOLD "))
    memory_threshold = int(input("ENTER THE MEMORY THRESHOLD "))

#comapre the cputhreshold value ith current value 
    if(cpu_threshold > psutil.cpu_percent(interval=1)):
        print("WARNING !")
    else:
        print("CPU IS IN SAFE STATE")

    if(memory_threshold > psutil.virtual_memory().percent):
        print("WARNING !")
    else:
        print("SAFE")
    
    if(disk_threshold > psutil.disk_usage('/').percent):
        print("WARNING")
    else:
        print("SAFE")
system_health()        