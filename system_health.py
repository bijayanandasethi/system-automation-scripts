import psutil
import datetime

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0

def check_system_health():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    print(f"[{now}] System Health Check")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        print(f"⚠️ ALERT: High CPU Usage detected! ({cpu_usage}%)")
    
    if memory_usage > MEMORY_THRESHOLD:
        print(f"⚠️ ALERT: High Memory Usage detected! ({memory_usage}%)")

if __name__ == "__main__":
    check_system_health()
