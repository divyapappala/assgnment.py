import json
class Employee:
    def __init__(self,id,first_name,middle_name,last_name):
        self.id=id
        self.f_name=first_name
        self.m_name=middle_name
        self.l_name=last_name
    def generate_mail(self):
        new_dict={}
        for employee in data ["employee"]:
            if employee in ['middle_name'] != "Null":
                full_name =employee ['first_name']+employee ['middle_name']+employee ['last_name']
                mail=f"{employee['id']}.{employee['first_name']}{employee['middle_name']}{employee['last_name']}company@gmail.com"
            else:
                full_name =employee['first_name'] + employee ['last_name']
                mail=f"{employee['id']}.{employee['first_name']}{employee['last_name']}company@gmail.com"
                new_dict[mail] = {"id":employee["id"],"fullname":full_name}
        return new_dict
file=open("data.json","r")
file_name=file.read()
data=json.loads(file_name)

for employee in data ["employee"]:
      a = Employee(**employee)
      s = a.generate_mail()
b = json.dumps(s,indent=2)      
print(b)


