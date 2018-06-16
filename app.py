from flask import Flask, request
import habits

app = Flask(__name__)


@app.route('/task/<task_content>')

def main(task_content):
    task_url = str(request.data)
    habits.main(task_url)
    return task_content


if __name__ == '__main__':
    app.run()
