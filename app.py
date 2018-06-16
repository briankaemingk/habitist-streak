from flask import Flask
import habits

app = Flask(__name__)


@app.route('/task/<taskurl>')
def main(taskurl):
    habits.main(taskurl)

    return taskurl


if __name__ == '__main__':
    app.run()
