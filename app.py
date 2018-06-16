from flask import Flask, request
import habits

app = Flask(__name__)


@app.route('/task/<task_content>')
def main(task_content):
    habits.main(task_content)
    data = request.data
    print (data)

    return task_content


if __name__ == '__main__':
    app.run()
