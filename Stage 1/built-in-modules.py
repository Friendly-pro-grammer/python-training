#------Math-Module---------
import math
print(math.pi,math.e)
print(math.sqrt(6))
print(math.pow(2,3))
print(math.fabs(-19))
print(math.ceil(3.4234))
print(math.floor(43.34243))
print(math.factorial(5))
print(math.gcd(10,25))
print(math.lcm(2,20,60))
print(math.sin(90))
print(math.log(20))


#-----random----module------
import random
print(math.floor(random.random()*10))
print(random.randint(1,10))
print(random.randrange(1,11))
names=["amit","yadav","gec","modasa"]
print(random.choice(names))
print(random.choices(names,k=2))
print(random.sample([x for x in range(1,100)],10))
res =random.shuffle(names)
print(res)


#--------os-module-----
import os
print(os.getcwd())
print(os.listdir())
os.mkdir("data")
os.rmdir("data")
print(os.path.exists("Stage1"))

path = os.path.join("data","users","users.csv")
print(path)

print(os.path.basename(path))
print(os.path.dirname(path))

#--------date-time-module-------
import datetime
now = datetime.datetime.now()
print(now)
date = datetime.datetime.today()
print(date)
from datetime import date,datetime
d =date(2026,8,18)
print(d)
dt = datetime(2026,8,18,22,30,11)
print(dt)
nows = datetime.now()
print(nows.year)
print(nows.month)
print(nows.day)

print(nows.hour)
print(nows.minute)
print(nows.second)

formatted = now.strftime("%d-%m-%Y")
print(formatted)
