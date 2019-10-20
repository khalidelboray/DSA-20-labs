from Classes import *
import json
i = 1
off = Office('Main Office')
info = {}
while i < 5:
    car = Car("Car " + str(i),80,100)
    empl = Employee("Empl"+str(i),2000,'lazy',80,i,car,"email"+str(i)+"@mail.com",2500,2000)
    #empl.drive(500)
    off.hire(empl)
    print(off.get_employee(i).name+ " Is Hired")
    print(empl.car.velocity)
    if off.check_lateness(i,7):
        print("{} is late his salary became {}".format(empl.name, empl.salary))
    i += 1
def to_json(office):
    info[office.name] = {}
    for emp in office.employees:
        dic = emp.__dict__
        #print(dic.keys())
        final = {}
        for x in ['name', 'mood', 'healthRate', 'money', 'id', 'email', 'salary', 'distanceToWork']:
            final[x] = dic[x]
        final['car'] = emp.car.__dict__
        info[office.name].setdefault('employees',[]).append(final)
    json_str = json.dumps(info, indent=4,ensure_ascii=False)
    print(json_str)
    return json_str
jsonstr = to_json(off)    
with open('office.json', 'w') as outfile:
    outfile.write(jsonstr)