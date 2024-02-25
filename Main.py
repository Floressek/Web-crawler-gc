import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

#Group number
group = 'WCY22IY5S1'

# Dictionary mapping blocks to hours
block_hours = {
    "block1": {"START": "08:00", "END": "09:35"},
    "block2": {"START": "09:50", "END": "11:25"},
    "block3": {"START": "11:40", "END": "13:15"},
    "block4": {"START": "13:30", "END": "15:05"},
    "block5": {"START": "15:45", "END": "17:20"},
    "block6": {"START": "17:35", "END": "19:10"},
    "block7": {"START": "19:25", "END": "21:10"}
}
# Adding a constant value - location
location = "academic grounds"

# URL of the academic schedule page
url = f'https://old.wcy.wat.edu.pl/pl/rozklad?grupa_id={group}'

# Set a User-Agent header to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...'  # Fill with actual one (safety purposes) 
}

try:
    # Send an HTTP GET request without verifying SSL certificates
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate all the lesson div elements
        lesson_divs = soup.find_all('div', {'class': 'lesson'})

        schedule_data = []

        for lesson_div in lesson_divs:
            date = lesson_div.find('span', {'class': 'date'}).text.strip()
            block_id = lesson_div.find('span', {'class': 'block_id'}).text.strip()
            name = lesson_div.find('span', {'class': 'name'}).text.strip()
            info = lesson_div.find('span', {'class': 'info'}).text.strip()
            color = lesson_div.find('span', {'class': 'colorp'}).text.strip()
            teacher_initials = lesson_div.find('span', {'class': 'sSkrotProwadzacego'}).text.strip()

            # Check if the block_id is in the block_hours dictionary
            if block_id in block_hours:
                start_time = block_hours[block_id]['START']
                end_time = block_hours[block_id]['END']
            else:
                start_time = "N/A"
                end_time = "N/A"

            # Convert date to the 'DD/MM/YYYY' format
            date = datetime.strptime(date, '%Y_%m_%d').strftime('%d/%m/%Y')

            # Convert start and end times to 'h:mmA' format (e.g., '11:25AM')
            start_time = datetime.strptime(start_time, '%H:%M').strftime('%I:%M %p')
            end_time = datetime.strptime(end_time, '%H:%M').strftime('%I:%M %p')

            lesson_info = {
                'Subject': name,
                'Start Date': date,
                'Start Time': start_time,
                'End Date': date,
                'End Time': end_time,
                'All Day Event': False,
                'Description': info,
                'Location': location,
                'Private': True,
            }

            schedule_data.append(lesson_info)

            # Get today's date as a datetime object
            today_date = datetime.now()

            # Filter lessons based on their start dates
            filtered_schedule_data = [lesson for lesson in schedule_data if datetime.strptime(lesson['Start Date'], '%d/%m/%Y') >= today_date]

        # Save the filtered data to a CSV file
        csv_filename = 'academic_scheduleG_filtered.csv'
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description', 'Location', 'Private']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for lesson in filtered_schedule_data:
                writer.writerow(lesson)

        print(f'Data saved to {csv_filename}')
    else:
        print('Failed to retrieve the page')

except Exception as e:
    print("An error occurred:", e)
