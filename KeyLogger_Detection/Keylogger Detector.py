import os
import psutil
import win32api
import win32con
import win32clipboard
import time
import csv

# Define the file path to monitor
file_path = "C:\\Users\\ksrey\\PycharmProjects\\Keylogger_Detection" # Enter the file path you want your files to be saved to
extend = "\\"  # replace with the desired directory

# Keep track of detected suspicious files
detected_files = set()

def monitor_system_activity():
    # Monitor system processes and look for suspicious activity
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'python.exe' and 'keylogger' in proc.cmdline():
                print("Suspicious keylogger process detected!")
                # Take action, such as terminating the process or alerting the user
        except psutil.NoSuchProcess:
            pass

def monitor_file_system_activity():
    global detected_files
    # Monitor file system activity and look for suspicious file creations
    for file in os.listdir(file_path):
        if file.endswith('.txt') or file.endswith('.wav') or file.endswith('.png'):
            if file not in detected_files:
                print("Suspicious file creation detected!")
                detected_files.add(file)
                # Take action, such as deleting the file or alerting the user
                with open('suspicious_files.csv', 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([file])

def monitor_clipboard_activity():
    # Monitor clipboard activity and look for suspicious data
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if len(data) > 100:  # arbitrary threshold
            print("Suspicious clipboard data detected!")
            # Take action, such as clearing the clipboard or alerting the user
    except win32api.error:
        pass

if __name__ == '__main__':
    while True:
        monitor_system_activity()
        monitor_file_system_activity()
        monitor_clipboard_activity()
        time.sleep(1)  # adjust the sleep interval as needed