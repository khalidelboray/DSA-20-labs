import re
from datetime import datetime
import time


class Person:
    __moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.mood = mood
        if 0 < healthRate <= 100:
            self.healthRate = healthRate
        else:
            raise Exception('Invalid helthRate')
        self.money = money
        self.mood = mood

    def sleep(self, hours):
        if hours == 7:
            self.mood = self.__moods[0]
        elif hours < 7:
            self.mood = self.__moods[1]
        elif hours > 7:
            self.mood = self.__moods[2]

    def eat(self, meals):
        if int(meals) <= 3:
            self.healthRate = 100
        elif int(meals) == 2:
            self.healthRate = 75
        elif int(meals) == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= 100 * items


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary,
                 distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        if type(car) is Car:
            self.car = car
        else:
            raise Exception("car must be of Type Car ")

        if re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
            self.email = email
        else:
            print("Email is not valid")
            exit(1)
        if salary >= 1000:
            self.salary = salary
        else:
            print("salary must be 1000 or more")
            exit(1)
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = self.__moods[0]
        if hours > 8:
            self.mood = self.__moods[1]
        if hours < 8:
            self.mood = self.__moods[2]

    def send_mail(self, to, subject, msg, receiver_name):
        message = "From: {}\nTo: {}\n\n   Hi, {}\n{subject}\n".format(
            self.email, to, receiver_name, subject=msg)
        time = datetime.now().strftime("%H.%M.%S")
        f = open("mail_" + time + ".txt", 'a')
        f.write(message)
        f.close

    def drive(self, distance):
        self.car.run(100, distance)
        self.distanceToWork -= distance

    def refuel(self, gasAmount):
        if self.car.fuelRate < 100:
            if gasAmount > (100 - self.car.fuelRate):
                self.car.fuelRate = 100
                return
            self.car.fuelRate += gasAmount
        else:
            pass


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.set_fuelRate(fuelRate)
        self.set_velocity(velocity)

    def set_fuelRate(self, fuelRate):
        if fuelRate <= 100:
            self.fuelRate = fuelRate
        else:
            raise Exception("fuelRate must be between 0 to 100")

    def set_velocity(self, velocity):
        if velocity <= 200:
            self.velocity = velocity
        else:
            raise Exception("velocity must be between 0 to 200")

    def run(self, velocity, distance):
        self.set_velocity(velocity)
        rem = -1
        while 1:
            if self.fuelRate == 0 or rem == 0:
                self.stop(rem)
                break
            time.sleep(1)
            self.fuelRate -= 10
            distance -= velocity
            rem = distance

    def stop(self, remain):
        #self.set_velocity(0)
        if remain == 0:
            print("{} arrived the destintation ".format(self.name))
        else:
            print("The remain distance for {} is {}".format(self.name,remain))


class Office:
    __empls = {}

    def __init__(self, name):
        self.name = name

    @property
    def employees(self):
        return self.get_all_employees()

    def get_all_employees(self):
        return list(self.__empls.values())

    def get_employee(self, empId):
        if empId in self.__empls.keys():
            return self.__empls[empId]
        else:
            raise Exception("EmpId not found")

    def hire(self, Emp):
        if type(Emp) is Employee:
            self.__empls.update({Emp.id: Emp})
        else:
            raise Exception("Emp attr must be of Type Employee")

    def fire(self, empId):
        if empId in self.__empls.keys():
            del self.__empls[empId]
        else:
            raise Exception("We Didn't Hire him ")

    def deduct(self, empId, deduction):
        if empId in self.__empls.keys():
            self.get_employee(empId).salary -= deduction
        else:
            raise Exception("EmpId not found")

    def reward(self, empId, reward):
        if empId in self.__empls.keys():
            self.get_employee(empId).salary += reward
        else:
            raise Exception("EmpId not found")

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if self.calculate_lateness(8, moveHour, emp.distanceToWork,
                                   emp.car.velocity):
            self.deduct(empId, 10)
            return 1
        else:
            self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if distance == 0:
            return 1 
        return (distance / velocity) > (targetHour - moveHour)

    def change_emps_num(self, num):
        pass