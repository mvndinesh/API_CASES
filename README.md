Activity: I was given an activity to validate the gemini new order api. I was provided following base url and the end point.
#Base_url
BASE_URL = "https://api.sandbox.gemini.com"
#New Order
NEW_ORDER = '/v1/order/new'

#Python Features
To automate the API cases for the above endpoint I have utilized the unittest and pytest features.
The folder structure is segegrated and organized for easy maintainence.

#Folder Structure
api_responses : This folder has the response classes wheere the response is passed to these classes. The instance of these classes are returned to the test scripts for validation.

payloads_json: This folder consist of all the required request json files for testing.

rest_api : Instead of directly using the requests feature in python, I have created the base_api file to maintain all the api requests such as post, get etc. We can call these static methods from this class where ever it is rquired

test_scripts_api : Folder to maintain all the api test scripts.example : test_gemini_order.py

workflows : This folder is used to store the required workflows related to a functionaity. For example, all the new order related workflows will be stored in this python file. This will reduce the redundancy and effective usage of functions.

common_methods : All the common methods used accross the python files in this project are placed here. For example, read json, assert functions.

constants : All the constants used accross this project are stored here.

endpoints : All the base urls and endpoints are stored here.

requirements.txt : Basics installations are stored here to create the virtual environment and run these dependencies usng the commmand pip3 install -r requirements.txt

logs : path --> API_CASES/test_scripts_api/app.log 

#To execute the test cases :

Navigate to the test_scripts_api folder, right click on the test_gemini_order.py
and click on run.


