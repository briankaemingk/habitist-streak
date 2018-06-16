from flask import Flask, request
import habits

app = Flask(__name__)


@app.route('/')
def index():
    task_url = str(request.data)
    habits.main(task_url)
    return 'Completed.'

@app.route('/daily_check')
def daily_check():
    return 'Hello, World'


if __name__ == '__main__':
    app.run()
