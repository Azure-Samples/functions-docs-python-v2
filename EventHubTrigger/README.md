To test the Event Hub Trigger:

1. Within your Azure environment, create an **Event Hub Instance** and an underlying **Event Hub**.
2. Under the **Event Hub** resource, create a **Shared Access Key**.
3. Copy the **Connection String** value found in the new key you just created.
4. Paste it as part of your Function App's Configuration (localhost.json, if you are testing locally)
5. Copy and paste the **Event Hub Name** under the Function App's Configuration.

To upload sample data to your Azure Event Hub and see it processed from your Function App's code, under the **UploadToEventHub.py** file:

1. Copy and paste the Shared Access Key's **Connection String** and **Event Hub Name** in the appropriate locations in the **producer** variable (line 9).
2. Update the **directory** to the file: **SampleJsonFile.json** (line 13)
3. Optional: The 2 **for** loops can have their variables adjusted to send **i** batches of data and **j** data records. i.e. i = 3 batches, j = 5 data records, Total: 15 data records will be sent, split between 3 batches.
4. Using Cmd or PowerShell, navigate to the **UploadToEventHub.py** file's directory.
5. To execute the code, type into the console: **python .\UploadToEventHub.py**.