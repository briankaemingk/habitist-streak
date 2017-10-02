import os
import re
from pytodoist import todoist


def get_token():
    token = os.getenv('TODOIST_APIKEY')
    return token


def is_habit(text):
    return re.search(r'\[day\s(\d+)\]', text)


def main():
    API_TOKEN = get_token()
    if not API_TOKEN:
        print "Please set the API token in environment variable."
        exit()
    user = todoist.login_with_api_token(API_TOKEN)
    tasks = user.search_tasks(todoist.Query.TOMORROW)
    for task in tasks:
        habit = is_habit(task.content)
        if habit:
            streaks = int(habit.group(1)) + 1
            days = '[day {}]'.format(streaks)
            task.content = re.sub(r'\[day\s(\d+)\]', days, task.content)
            task.update()
        tasks = user.search_tasks(todoist.Query.OVERDUE)

    tasks = user.search_tasks(todoist.Query.OVERDUE)
    for task in tasks:
        habit = is_habit(task.content)
        if habit:
            streaks = 0
            days = '[day {}]'.format(streaks)
            task.content = re.sub(r'\[day\s(\d+)\]', days, task.content)
            task.date_string = 'ev day starting tod'
            task.update()


if __name__ == '__main__':
    main()
