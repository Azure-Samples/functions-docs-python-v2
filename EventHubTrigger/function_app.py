import azure.functions as func
import logging

app = func.FunctionApp()

# Decorators 'event_hub_name' and 'connection' pull their values from the configuration.
@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventHubName",
                               connection="connectionString")
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                azeventhub.get_body().decode('utf-8'))
