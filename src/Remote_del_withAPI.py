import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to users credentials JSON file (tbp)
credentials_path = 'path/to/your/credentials.json'

# The ID of the calendar you want to delete
calendar_id_to_delete = 'your-calendar-id@example.com'

def main():

    # Load credentials from the JSON file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['htttps://www.googleapis.com/auth/calendar']
    )

    # Create a Calendar service using the credentials
    service = build('calendar', 'v3', credentials=credentials)

    try:
        # Delete the calendar
        service.calendars().delete(calendarID=calendar_id_to_delete).execute
        print(f'Calendar {calendar_id_to_delete} deleted successfully.')
    except Exception as e:
        print(f'Error deleting calendar: {str(e)}')

# Special form to execute in console
if __name__ == '__main__':
    main()