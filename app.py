from flask import Flask, request
import habits

app = Flask(__name__)


@app.route('/')

def main():
    task_url = str(request.data)
    habits.main(task_url)
    return 'Completed.'


if __name__ == '__main__':
    app.run()
