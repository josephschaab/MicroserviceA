# Image processor microservice communication contract

This image processing microservice can have GET, POST, and DELETE functionality used for the data packages it processes. The data packagees hold image URL's that can be received, requested and deleted by the microservice. This microservice uses REST API, sending data through JSON packages. The REST API initially runs on http://127.0.0.1:5000. The address and port can be changed easily by modifying the ADDRESS and PORT variables in the main.py function.

## Requesting data programmatically from the microservice

To request data from this microservice, initially make sure you have imported the requests library.
Once requests has been imported, data can requested in the following format:
```BASE = ADDRESS +  ":" + PORT + "/"```
```response = requests.get(BASE + "image/" + str(i)) # i = image_id number```
This will request the data from the microservice correlating to the image_id number inputted in the request.

## Receiving data programmatically from the microservice

For the microservice to receive data, you will also need to make sure you have imported the requests library.
Once requests has been imported, data can be received in the following format:
```BASE = ADDRESS +  ":" + PORT + "/"```
```data = [{"name": "image0", "image_url": "abc"}]```
```response = requests.post(BASE + "image/" + str(i), data[0]) # i = image_id number```
This format will send data to be received by the microservice. Data must follow json package formatting with "name" and "image_url" string values provided.

## UML sequence diagram
![UML sequence diagrma](https://github.com/josephschaab/MicroserviceA/blob/main/Images/UML_diagram_intial.png)




