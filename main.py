import mysql.connector as mysql
import random
from geopy import distance
con=mysql.connect(host='localhost', user='root',password='password',database='flight_game')
cursor=con.cursor()
current_airport=None
print('<game description>')
#create table credentials(name varchar(20),password varchar(20));
def validation():
    username = input('enter username')
    password = input('enter password')
    querry='select * from credentials'
    cred=(username,password)
    cursor.execute(querry)
    data=cursor.fetchall()
    for i in data:
        if i==cred:
            return True
    else:
        return False
def new_user():
    username = input('enter username')

    querry = 'select name from credentials;'
    cursor.execute(querry)
    data = cursor.fetchall()

    for i in data:
        if i[0] == username:
            return False
    else:
        password = input('enter password')
        querry=f'insert into credentials values("{username}","{password}");'
        cursor.execute(querry)
        con.commit()
        return True
def starting_airport():
    global current_airport
    a=random.randint(1,70942)
    querry='select name from airport;'
    cursor.execute(querry)
    b=cursor.fetchall()
    current_airport=b[a][0]
    return current_airport
def airportscloseby():
    global current_airport
    querry1='select name,latitude_deg,longitude_deg from airport;'
    cursor.execute(querry1)
    a=cursor.fetchall()
    querry2=f'select latitude_deg,longitude_deg from airport where name="{starting_airport()}"'
    cursor.execute(querry2)
    data=cursor.fetchone()
    for i in a:
        loc1 = data
        loc2 = (i[1], i[2])
        distanc=distance.distance(loc1, loc2).miles
        if distanc<10:
            print(i[0])
    current_airport=input('copy and paste the airport you want to go to')

airportscloseby()
airportscloseby()












