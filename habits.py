from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import os
import re
import logging
from datetime import datetime, timedelta
from todoist.api import TodoistAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_token():
    token = os.getenv('TODOIST_APIKEY')
    return token


def is_habit(text):
    return re.search(r'\[streak\s(\d+)\]', text)
    #return re.search(r'\[day\s(\d+)\]', text)


def is_today(text):
    today = (datetime.utcnow() + timedelta(1)).strftime("%a %d %b")
    return text[:10] == today


def is_due(text):
    yesterday = datetime.utcnow().strftime("%a %d %b")
    return text[:10] == yesterday


def update_streak(item, streak):

    days = '[day {}]'.format(streak)
    text = re.sub(r'\[day\s(\d+)\]', days, item['content'])
    item.update(content=text)


def main(task_url):
    API_TOKEN = get_token()
    today = datetime.utcnow().replace(tzinfo=None)

    #TODO URL is in format: https://todoist.com/showTask?id=2690174754
    task_match = re.search('https:\/\/todoist.com\/showTask\?id=([0-9]+)', task_url)
    task_id = task_match.group(0)
    #print (task_id)

    if not API_TOKEN:
        logging.warn('Please set the API token in environment variable.')
        exit()
    api = TodoistAPI(API_TOKEN)
    api.sync()
    tasks = api.state['items']
    for task in tasks:
        if task['due_date_utc'] and is_habit(task['content']):
            #print(task)
            if not is_today(task['due_date_utc']):
                print(task)
                habit = is_habit(task['content'])
                streak = int(habit.group(1)) + 1
                update_streak(task, streak)
            elif is_due(task['due_date_utc']):
                update_streak(task, 0)
                task.update(date_string='ev day starting tod')
    api.commit()

if __name__ == '__main__':
    main()