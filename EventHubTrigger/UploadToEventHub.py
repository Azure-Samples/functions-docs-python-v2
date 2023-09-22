# Author: Vijay Kumar Sude (alias: vsuda@microsoft.com)

import asyncio
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="{Event_Hub_Connection_String}", eventhub_name="{Event_Hub_Name}")
    
    async with producer:
        # Opening JSON file
        f = open('{My_Directory}/SampleJsonFile.json')
        
        # returns JSON object as a dictionary
        data = json.load(f)

        # Convert the data into a JSON string.
        s = json.dumps(data)
        
        # Closing file
        f.close()

        for i in range(0, 1):
            # Create a batch of 5 records.
            event_data_batch = await producer.create_batch()
            for j in range (0, 5):
                # Add events to the batch.
                try:
                    event_data_batch.add(EventData(s))
                except:
                    print("NameError: x is not defined.")
                    break
                # Send the batch of events to the event hub.
            await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())