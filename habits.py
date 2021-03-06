from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
from datetime import datetime, timedelta
import os
import re
import logging
from todoist.api import TodoistAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_token():
    token = os.getenv('TODOIST_APIKEY')
    return token

def is_habit(text):
    return re.search(r'\[streak\s(\d+)\]', text)

def update_streak(item, streak):
    streak_num = '[streak {}]'.format(streak)
    text = re.sub(r'\[streak\s(\d+)\]', streak_num, item['content'])
    item.update(content=text)

def parse_task_id(task_url):
    #URL is in format: https://todoist.com/showTask?id=2690174754
    task_match = re.search('https:\/\/todoist.com\/showTask\?id=([0-9]+)', task_url)
    task_id = task_match.group(1)
    return task_id

def is_due(text):
    yesterday = datetime.utcnow().strftime("%a %d %b")
    return text[:10] == yesterday

def increment_streak(api, task_url):
    tasks = api.state['items']
    for task in tasks:
        if int(task['id']) == int(parse_task_id(task_url)) and is_habit(task['content']):
            habit = is_habit(task['content'])
            streak = int(habit.group(1)) + 1
            update_streak(task, streak)
    api.commit()

def reset_streak(api):
    tasks = api.state['items']
    for task in tasks:
        if task['due_date_utc'] and is_habit(task['content']) and is_due(task['due_date_utc']):
            update_streak(task, 0)
            date_string = task['date_string']
            task.update(date_string= date_string + ' starting tod')
    api.commit()

def main():
    API_TOKEN = get_token()
    if not API_TOKEN:
        logging.warn('Please set the API token in environment variable.')
        exit()
    api = TodoistAPI(API_TOKEN)
    api.sync()
    return api


if __name__ == '__main__':
    main()