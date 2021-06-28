# Selenium + Redis Example

This is an example of using Selenium with Redis and Flask. The purpose of this is to save session with Selenium. You may want to do this for a few reasons: 
 - Save login session
	 - Very useful for saving Captcha or ReCaptcha session 
 - Applications that have many Selenium calls can use one instance instead of creating many, saving resources
 - Scheduling tasks that can be completed with Selenium

# How to run locally

 1. Git clone this repository 
 2. Ensure that Redis is downloaded locally (see Brew instructions)
 3. cd into repo's root
 4. Run `python3 -m venv env` - this is to create the virtual environment
 5. Run `source env/bin/activate` - this is to enter the virtual environment (you'll have to run this command for every new terminal window you create)
 6. Run `pip install -r requirements.txt`to install the requirements/dependencies for this project
 7. Now, we can start the servers. **You'll need 3 terminal windows which are in the virtual environment.** 
 8. First terminal window, run `flask run`(starts Flask server to handle requests and add tasks to queue)
 9. Second, run `redis-server`(starts Redis server) 
 10. Third, run `python red.py`(starts Redis worker to listen and queue tasks based on requests sent) (**Make sure you are in the virtual environment on your newly opened window or else you will get an error that says Redis module could not be found.**)

From this point, you can use Postman or an application of your choice to hit the flask API endpoints. 

   

    GET http://127.0.0.1:5000/run - This will start Selenium instance
    GET http://127.0.0.1:5000/run2 - This will open Github
    GET http://127.0.0.1:5000/run3 - This will open StackOverflow
**Try this:** Send many (run2 and run3) requests within a few seconds. You will see that Redis is adding each request to the queue and ONLY when a task is finished, it will move onto the next task. 

## What's the point of this?

As described earlier, the problem this solves is not opening a new Selenium driver for each task it needs to do. And, task queuing is also handled so many requests can be sent to Selenium and it will do the tasks as it can. 

Try a few things!
1. Change the link from github to google. Upon saving your code, /run2 will immediately take you to google. No more stopping Selenium to effect code changes.
2. Queue up a bunch of functions and watch in the red.py window how tasks are being done in queue order.
