from flask import Flask, render_template, request
import habits

app = Flask(__name__)


@app.route('/')
def main():
    habits.main()
    return "Completed."


if __name__ == '__main__':
    app.run()
