import os
import re
import logging
from datetime import datetime, timedelta
from pytodoist import todoist

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_token():
    token = os.getenv('TODOIST_APIKEY')
    return token


def is_habit(text):
    return re.search(r'\[day\s(\d+)\]', text)


def update_streak(task, streak):
    days = '[day {}]'.format(streak)
    task.content = re.sub(r'\[day\s(\d+)\]', days, task.content)
    task.update()


def main():
    API_TOKEN = get_token()
    today = datetime.utcnow().replace(tzinfo=None)
    
    if not API_TOKEN:
        logging.warn('Please set the API token in environment variable.')
        exit()
    user = todoist.login_with_api_token(API_TOKEN)
    
    #Check for Overdue
    project = user.get_project('Habbits')    
    tasks = project.get_completed_tasks()
    for task in tasks:
        
        habit = is_habit(task.content)
        if habit:
        content = task.content
        due = datetime.strptime(task.due_date_utc, '%a %d %b %Y %H:%M:%S %z').replace(tzinfo=None)
        complete = task.checked
        
        print('Found Task:' + content)
        print(due)
        print(complete)
        
        if habit and complete == 1:
            streak = int(habit.group(1)) + 1
            update_streak(task, streak)
        
        if habit and today > due and complete == 0:
            task.date_string = 'ev day starting tod'
            update_streak(task, 0)
            
if __name__ == '__main__':
    main()
