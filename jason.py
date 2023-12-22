# Import JSON module
import json
 
# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
 
# Convert JSON String to Python
student_details = json.loads(jsonString)
 
# Print Dictionary
print(student_details)
 
# Print values using keys
print(student_details['name'])
print(student_details['course'])


# # Python program to demonstrate
# # Conversion of JSON data to
# # dictionary
 
# # importing the module
# import json
 
# # Opening JSON file
# with open('data.json') as json_file:
#     data = json.load(json_file)
 
#     # Print the type of data variable
#     print("Type:", type(data))
 
#     # Print the data of dictionary
#     print("\nPeople1:", data['people1'])
#     print("\nPeople2:", data['people2'])

import json 

# JSON string 
employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'} 
print("This is Python", type(employee_dict)) 

print("\nNow Convert from Python to JSON") 

# Convert Python dict to JSON 
json_object = json.dumps(employee_dict, indent=4) 
print("Converted to JSON", type(json_object)) 
print(json_object) 
