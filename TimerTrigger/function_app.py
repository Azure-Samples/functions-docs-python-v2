import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# A timer trigger function which repeats every 5 seconds and only accepts HTTP "GET" and "POST" requests.
@app.timer_trigger(schedule="5 * * * * *", arg_name="myTimer", methods=["GET", "POST"], run_on_startup=True,
              use_monitor=False) 
def TimerTrigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')