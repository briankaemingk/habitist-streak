from flask import Flask, request
import habits

app = Flask(__name__)

@app.route('/')
def index():
    print('here')
    api = habits.main()
    task_url = str(request.data)
    habits.increment_streak(api, task_url)
    return 'Completed increment streak.'

@app.route('/reset_streak')
def reset_streak():
    api = habits.main()
    habits.reset_streak(api)
    return 'Completed reset streak.'

if __name__ == '__main__':
    app.run()
