import csv
import psutil

# Collect process information
process_data = []
for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
    try:
        info = proc.info
        process_data.append({
            'Process Name': info['name'],
            'Memory Usage': info['memory_info'].rss,
            'CPU Usage': info['cpu_percent'],
            # Add more features as needed
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Save process data to a CSV file
with open('task_manager_snapshot.csv', 'w', newline='') as csvfile:
    fieldnames = ['Process Name', 'Memory Usage', 'CPU Usage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in process_data:
        writer.writerow(data)