from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import os
import re
from todoist.api import TodoistAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_token():
    token = os.getenv('TODOIST_APIKEY')
    API_TOKEN = get_token()
    if not API_TOKEN:
        logging.warn('Please set the API token in environment variable.')
        exit()
    return token

def is_habit(text):
    return re.search(r'\[streak\s(\d+)\]', text)

def update_streak(item, streak):
    streak_num = '[streak {}]'.format(streak)
    text = re.sub(r'\[streak\s(\d+)\]', streak_num, item['content'])
    item.update(content=text)

def increment_streak(api, task_url):
    tasks = api.state['items']
    #URL is in format: https://todoist.com/showTask?id=2690174754
    task_match = re.search('https:\/\/todoist.com\/showTask\?id=([0-9]+)', task_url)
    if(task_match) :
        task_id = task_match.group(1)
        for task in tasks:
            if int(task['id']) == int(task_id) and is_habit(task['content']):
                habit = is_habit(task['content'])
                streak = int(habit.group(1)) + 1
                update_streak(task, streak)
    api.commit()

def reset_streak(api):
    api.commit()

def main(task_url):
    api = TodoistAPI(get_token())
    api.sync()
    return api


if __name__ == '__main__':
    main()