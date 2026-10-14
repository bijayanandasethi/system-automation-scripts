import shutil
import psutil

print("--- System Health Report ---")
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")
