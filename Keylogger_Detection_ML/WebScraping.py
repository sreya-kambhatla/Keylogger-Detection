# Web scraping Windows process names using requests
import requests
from bs4 import BeautifulSoup
import csv

def get_directory_names(base_url, letter):
    """
    Fetch process names from the website and return a list of names.
    """
    process_names = []
    page = 1
    while True:
        try:
            url = f"{base_url}/{letter}/{page}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            if "No processes" in response.text:
                break
            soup = BeautifulSoup(response.text, 'lxml')
            directory_items = soup.find_all("td", class_="process")
            process_names.extend([item.text.strip() for item in directory_items])
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break
    return process_names

def save_to_csv(process_names, filename):
    """
    Save the list of process names to a CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[row] for row in process_names])

# Parameters
base_url = "https://www.processlibrary.com/en/directory"
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
filename = "process_directory.csv"

# Function Calls
process_names = []
for letter in letters:
    process_names.extend(get_directory_names(base_url, letter))

save_to_csv(process_names, filename)

print(f"Data has been written to {filename}")