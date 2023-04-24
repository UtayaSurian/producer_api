# Producer API

### The Producer API acts as a RabbitMQ publisher. It is responsible to accept POST message from sender, process it and publish into  RabbitMQ queue server.

The entire producer API was written using Django Rest API concept.

Example on how to send request to this API:

**Endpoint**: http://127.0.0.1:8000/process-data/

**Sample Input:**

_{
   "device_id":"",
   "client_id":"",
   "created_at":"",
   "data":{
      "license_id":"1fdbb175-81d3-4062-b76d-d274674348e9",
      "preds":[
         {
            "image_frame":"QW55IGltYWdlIGZyYW1lcyBmcm9tIHNlbmRlcg==",
            "prob":"0.23",
            "tags":[]
         }
      ]
   }
}_