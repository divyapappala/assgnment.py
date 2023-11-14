import json


file = open("data.json","r")
file_name = file
data = json.load(file_name)
for employees in data["employees"]:
    first_name = employees['firstName']
    middle_name = employees['middleName']
    last_name = employees['lastName']
    if middle_name:
         email = f"{first_name}_{middle_name}.{last_name}@company.com"
    else:
         email = f"{first_name}.{last_name}@company.com"     
    print(email)
    employee_details=json.dumps(employees,indent=2)
    print(employee_details)