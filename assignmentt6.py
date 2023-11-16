import json


file = open("new.json","r")
file_name = file.read()
data = json.loads(file_name)
new_dict = {}
for employees in data["employees"]:
    first_name = employees['firstName']
    middle_name = employees['middleName']
    last_name = employees['lastName']
    if middle_name != None :
        email = f"{first_name}_{middle_name}.{last_name}@company.com"
        full_name = f"{first_name}{middle_name}{last_name}"
    else:
        email = f"{first_name}.{last_name}@company.com"
        full_name = f"{first_name}{last_name}"
    #new_dict = {}
    new_dict[email]={"id":employees["id"],"fullName":full_name}
employee_details=json.dumps(new_dict,indent=2)
print(employee_details)