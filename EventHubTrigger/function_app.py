import azure.functions as func
import logging

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventHubName",
                               connection="connectionString")
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                azeventhub.get_body().decode('utf-8'))
