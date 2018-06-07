import os
import json

location = os.path.abspath(os.path.dirname(__file__))

# Read all the user requests from file into a dictionary
user_requests_json_str = open(os.path.join(location,"json_test_files/user_requests.json")).read()
user_requests_data = json.loads(user_requests_json_str)

#Read a single user request from file into a dictionary
user_request_json_str = open(os.path.join(location,"json_test_files/user_request.json")).read()
user_request_data = json.loads(user_request_json_str)

#Read a user entry from a file - to be used in testing POST actions
#Note this is submitted user input, does not included request id.
user_entry_json_str = open(os.path.join(location,'json_test_files/user_entry.json')).read()
user_entry_data = json.loads(user_entry_json_str)

#Read a user entry from a file - to be used in testing POST actions
#Note this is submitted user input, does not included request id.
user_entry2_json_str = open(os.path.join(location,'json_test_files/user_entry2.json')).read()
user_entry2_data = json.loads(user_entry2_json_str)

#Read a new user to be registered from a file 
new_user1_json_str = open(os.path.join(location,'json_test_files/new_user1.json')).read()
new_user1_data = json.loads(new_user1_json_str)


#Read a single user request from file - used in testing POST when user adds request
#Note the request id is added
new_user_creation_success_json_str = open(os.path.join(location,'json_test_files/new_user_creation_success.json')).read()
new_user_creation_success = json.loads(new_user_creation_success_json_str)

# Read an entry to modify a user request
user_request_modify_json_str = open(os.path.join(location,'json_test_files/user_request_modify.json')).read()
user_request_modify_data = json.loads(user_request_modify_json_str)

# Read the user request modification result
user_request_modify_result_json_str = open(os.path.join(location,'json_test_files/user_request_modify_result.json')).read()
user_request_modify_result_data = json.loads(user_request_modify_result_json_str)
