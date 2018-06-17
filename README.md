# habitist (streak)  [![Code Climate](https://codeclimate.com/github/briankaemingk/habitist-streak/badges/gpa.svg)](https://codeclimate.com/github/briankaemingk/habitist-streak)
An automation to enable habit tracking in todoist. 

It integrates Seinfield's "[Don't Break the Chain](https://lifehacker.com/281626/jerry-seinfelds-productivity-secret)" method into [todoist](http://todoist.com/). Once it's setup, you can forget about it and it works seamlessly.

This is a different flavor of the originally implemented [habitist](https://github.com/amitness/habitist). While habitist is focused on daily habits, habitist (streak) can be applied to streaks of any recurrence time-frames (daily, weekly, monthly, etc).

## Usage

1. You add habits you want to form as task on todoist with a recurring schedule (could be any recurrance pattern (`every day`, `every week` or `every year`, for example)

2. Add `[streak 0]` to the task

3. When you complete the task, the `[streak 0]` will become `[streak 1]`

TODO: 4. If you fail to complete the task and it becomes overdue, the script will schedule it to today and reset `[streak X]` to `[streak 0]`.

## Installation
1. Fork and clone the repo
    ```
    git clone https://github.com/yourgithubusername/habitist-streak
    ```
2. Create a heroku app.
    ```
    heroku create appname
    ```
3. Set environment variable with your todost API key. You'll find API key under `Settings > Integrations` on [todoist.com](https://todoist.com).
    ```
     heroku config:set TODOIST_APIKEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ``` 

4. Push the app
    ```
    git push heroku master
    ```
 
5. On [IFTTT](http://ifttt.com/), [create](https://ifttt.com/create) a new applet. 
    - On THIS, select datetime > 'Every Day At' > 12 AM
    - On THAT, select Webhooks > Make a web request
    - Set URL to your heroku app URL with the directory`/reset_streak`:
    ```
    https://your-habitist-streak-app-name.herokuapp.com/reset_streak
    ```
    - Set METHOD to GET
    - Hit Create Action

6. On [IFTTT](http://ifttt.com/), [create](https://ifttt.com/create) a new applet.
    - On THIS, select todoist > 'New completed task' > Any Project 
    - On THAT, select Webhooks > `Make a web request`
    - Set URL to your heroku app URL
    - Set METHOD to GET
    - Hit Create Action

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
