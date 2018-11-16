#!/usr/bin/python

import MySQLdb


def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="localhost", user="root", passwd="Mofransi1", db="Dexxys")


'''Open database connection
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

#sql = "SELECT * FROM EMPLOYEE \
#     WHERE INCOME > '%d'" % (1000)'''


def getUser(id):
    db = connect()
    cur = db.cursor()

    # Execute the SQL command
    cur.execute("SELECT `surname`, `amount` FROM `customer` WHERE id = %s", (id))
    # Fetch all the rows in a list of lists.
    row = cur.fetchone()
    db.close()
    if row is None:
        return "No data fetched"
    else:
        return row[0] + "," + str(row[1])


def getMoney(id, amount, pin):
    db = connect()
    cur = db.cursor()
    # print("|" +str(pin) +"|")
    cur.execute("SELECT pin FROM customer WHERE id = %s", (id))
    row = cur.fetchone()
    # print("|"+str(row[0]) +"|")

    if row[0] is None:
        return "No such user has been created"
    elif row[0] == pin:
        cur.execute("SELECT amount FROM customer WHERE id = %s AND pin = %s ", (id, pin))
        account = cur.fetchone()
        print(account[0])
        if account[0] < amount:
            return "Not enough money in account"
        else:
            balance = account[0] - amount
            # print(balance)
            try:
                cur.execute("UPDATE customer SET amount = %s WHERE id = %s", (balance, id))
                db.commit()
                return "Balance is " + str(balance)
            except(MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                db.rollback()

    else:
        print("No such ")
    db.close()


def create(id, name, surname, amount):
    db = connect()
    cur = db.cursor()
    pin = 1234
    try:
        cur.execute("INSERT INTO customer (id, pin, name, surname, amount) VALUES (%s, %s, %s, %s, %s) ",
                    (id, pin, name, surname, amount))
        db.commit()
        db.close()
        return "Created"
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        var = db.rollback
        return "Error"


def addMoney(id, amount):
    user = getUser(id)
    surn, amt = user.split(',')
    #print(amt)
    balance = float(amt) + amount
    db = connect()
    cur = db.cursor()
    try:
        cur.execute("UPDATE customer SET amount = %s WHERE id = %s", (balance, id))
        db.commit()
        return "Money added"
    except(MySQLdb.Error, MySQLdb.Warning)as e:
        print(e)
        db.rollback()

# disconnect from server
# db.close()
