from __future__ import annotations
# 1 ************************************************
class Owner:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age
    
    def __str__(self):
        return f"name: {self.__name}\nsurname: {self.__surname}\nage: {self.__age}"

    def get_age(self):
        return f"age: {self.__age}"
    
    def get_name(self):
        return f"name: {self.__name}"
    
    def get_surname(self):
        return f"surname: {self.__surname}"

    def set_name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("fatal(, ne str")
        
    def set_surname(self, new_surname: str):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            raise TypeError("fatal(, ne str")
        
    def set_age(self, new_age: int):
        if isinstance(new_age, int):

            if new_age >= 18 and new_age < 150:
                self.__age = new_age
            else:
                print('вы либо слишком юны, либо уже умерли :(')

        else:
            raise TypeError("fatal(, ne int")

class BankAccount:
    def __init__(self, owner: Owner, balance: float):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner
    
    def get_balance(self):
        return f"balance: {self.__balance}"
    
    def set_balance(self, delta: float):
        if isinstance(delta, float):

            if (self.__balance + delta) >= 0:
                return self.__balance + delta
            else:
                return 'в долг не даем и вам не советуем!'
            
        else:
            raise TypeError('ne  float :()')
        
    def __str__(self):
        return (f"owner: {self.__owner}\n"
                f"balance: {self.__balance}")
        
user = Owner('lol', 'kek', 20)
acc = BankAccount(user, 15.1)
print(acc.get_balance())
print(acc.set_balance(-25.0))

#2 ********************************************************
class Rectangle:
    def __init__(self, height: float, width: float):
        self.__height = height
        self.__width = width

    def __str__(self):
        return (f"height: {self.__height}"
                f"width: {self.__width}")
    
    def get_height(self):
        return f"height: {self.__height}"
    
    def get_width(self):
        return f"width: {self.__width}"
    
    def set_height(self, delta: float):
        if isinstance(delta, float):

            if (self.__height + delta) > 0:
                return self.__height + delta
            else: return 'математика за пятый класс...'
        
        else:
            raise TypeError('ne float :()')
    
    def set_width(self, delta: float):
        if isinstance(delta, float):

            if (self.__width + delta) > 0:
                return self.__width + delta
            else: return 'математика за пятый класс...'
        
        else:
            raise TypeError('ne float :()')
        
    def area(self):
        return f"area: {self.__height * self.__width}"

rect = Rectangle(5.0, 4.0)
print(rect.get_height())
print(rect.set_height(-15.0))
print(rect.get_width())
print(rect.area())

# 3 **************************************************************
class People:
    def __init__(self, name: str, surname:str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f"name: {self.__name}\nsurname: {self.__surname}\nage: {self.__age}"

    def get_age(self):
        return f"age: {self.__age}"
    
    def get_name(self):
        return f"name: {self.__name}"
    
    def get_surname(self):
        return f"surname: {self.__surname}"

    def set_name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("fatal(, ne str")
        
    def set_surname(self, new_surname: str):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            raise TypeError("fatal(, ne str")
        
    def set_age(self, new_age: int):
        if isinstance(new_age, int):

            if new_age >= 5 and new_age < 20:
                self.__age = new_age
            else:
                print('вы либо слишком юны, либо пора задуматься...')

        else:
            raise TypeError("fatal(, ne int")


class Journal:
    def __init__(self):
        self.__math = []
        self.__russian = []
        self.__informatics = []

    def __repr__(self):
        return (f"math: {self.__math}; "
                f"russian: {self.__russian}; "
                f"informatics: {self.__informatics}; ")
    
    def append_math(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__math.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
    
    def append_rus(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__russian.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
        
    def append_inf(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__informatics.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
    
    def mean_math(self):
        if len(self.__math) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__math)):
            count += self.__math[i]

        return round(count / len(self.__math), 2)
    
    def mean_russian(self):
        if len(self.__russian) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__russian)):
            count += self.__russian[i]

        return round(count / len(self.__russian), 2)
    
    def mean_informatics(self):
        if len(self.__informatics) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__informatics)):
            count += self.__informatics[i]

        return round(count / len(self.__informatics), 2)


class Student:
    def __init__(self, people: People, class_stud: str, journal: Journal):
        self.__people = people
        self.__class_stud = class_stud
        self.__journal = journal

    def __repr__(self):
        return (f"student: \n{self.__people}\n"
                f"class: {self.__class_stud}\n"
                f"journal: \n{self.__journal}")


p1 = People('lol', 'kek', 12)
p1.set_age(15)
m = [2, 4, 5]
r = [2, 2, 2]
inf = [2, 4, 5]
jour = Journal()
jour.append_inf(4)
print('mean math: ', jour.mean_math())

stud = Student(p1, '2a', jour)
print(stud)

# 4 ***************************************************
class TemperatureLog:
    def __init__(self, city: str):
        self.__city = city
        self.__temperatures = [0, 0, 0, 0, 0, 0, 0]

    def __repr__(self):
        return (f"city: {self.__city}\n"
                f"temp: {self.__temperatures}")
    
    def get_city(self):
        return self.__city
    
    def set_city(self, city: str):
        if isinstance(city, str):
            self.__city = city
        else:
            raise TypeError('ne str :()')
        
    def get_temp(self):
        return self.__temperatures
    
    def check_index(self, index):
        if isinstance(index, int):
            
            if index >= 0 and index <= 6:
                return index
            else:
                raise ValueError('going out of range')
        
        else:
            raise TypeError('ne int (')
        
    def check_temp(self, temp):
        if isinstance(temp, int):
            
            if temp >= -100 and temp <= 100:
                return temp
            else:
                raise ValueError('going out of range temperature')
        
        else:
            raise TypeError('ne int (')

    def set_temp(self, new_temp: int, index: int):
        """
        0 - понедельник, 6 - воскресенье
        self.__temperatures = [0, 0, 0, 0, 0, 0, 0] по умолчанию
        """
        ind = self.check_index(index)
        temp = self.check_temp(new_temp)
        self.__temperatures[ind] = temp

        return self.__temperatures

    def average_temp(self):
        summ = 0
        for i in range(7):
            summ += self.__temperatures[i]

        return round(summ / 7, 2)
    
    def max_temp(self):
        maxx = self.__temperatures[0]
        for i in range(7):
            if self.__temperatures[i] > maxx:
                maxx = self.__temperatures[i]

        return maxx

    def min_temp(self):
        minn = self.__temperatures[0]
        for i in range(7):
            if self.__temperatures[i] < minn:
                minn = self.__temperatures[i]

        return minn

city = TemperatureLog(':3')
print(city)
city.set_temp(20, 0)
r = city.min_temp()
print(r)

# 5 ***************************************************
class People:
    def __init__(self, name: str, surname:str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f"name: {self.__name}\nsurname: {self.__surname}\nage: {self.__age}"

    def get_age(self):
        return f"age: {self.__age}"
    
    def get_name(self):
        return f"name: {self.__name}"
    
    def get_surname(self):
        return f"surname: {self.__surname}"

    def set_name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("fatal(, ne str")
        
    def set_surname(self, new_surname: str):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            raise TypeError("fatal(, ne str")
        
    def set_age(self, new_age: int):
        if isinstance(new_age, int):

            if new_age >= 16 and new_age < 100:
                self.__age = new_age
            else:
                print('вы либо слишком юны, либо пора задуматься...')

        else:
            raise TypeError("fatal(, ne int")
        
class EmployeePayroll:
    def __init__(self, people: People, salary: int,
                 tax_rate: float):
        self.__people = people
        self.__salary = salary
        self.__tax_rate = tax_rate
        
    def __str__(self):
        return (f"people: {self.__people}\n"
                f"salary: {self.__salary}\n"
                f"tax_rate: {self.__tax_rate}")
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new: int):
        if isinstance(new, int):

            if new >= 0:
                self.__salary = new
            else:
                raise ValueError('сотрудники не дают зп в долг')
            
        else:
            raise TypeError('ne int :3')
        
    def get_tax_rate(self):
        return self.__tax_rate
    
    def set_tax_rate(self, rate: float):
        if isinstance(rate, float):

            if rate >= 0 and rate <= 1:
                self.__tax_rate = rate
            else:
                raise ValueError('сотрудники не могут платить больше, чем заработали')
            
        else:
            raise TypeError('ne float :3')
        
    def net_salary(self):
        return round((self.__salary * (1 - self.__tax_rate)), 2)
    
    def annual_net(self):
        return 12 * self.net_salary()
    
people = People('lol', 'lol', 12)
nn = EmployeePayroll(people, 120, 0.5)
print(nn.annual_net())
print(nn.net_salary())