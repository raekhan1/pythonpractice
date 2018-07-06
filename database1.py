import sqlite3

def amend():
    with sqlite3.connect("CityTemperatures.db") as conn:
        cursor = conn.cursor()
        for row in cursor.execute("SELECT * FROM tblTemps"):
            print (row)
        keyfield = input("Enter city name of the record to amend: ")
        keyfield = "'" + keyfield + "'"

        field = input("Change which field \ (temperature or localTime)?")
        newvalue = input("Enter the new value for this field: ")

        try:
            cursor.execute ("UPDATE tblTemps SET " + field + "=" + newvalue + "WHERE city = " + keyfield)
            print("\nRecord updated")
        except:
            print("\nNo record updated - invalid data entered")

        for row in cursor.execute("SELECT * FROM tblTemps"):
            print (row)        

amend()




##def deleteRec(dbname):
##    conn=sqlite3.connect (dbname)
##    with conn:
##        cursor = conn.cursor()
##        myCity = input ("Enter name of city to delete: ")
##        keyfield = "'" + myCity + "'"
##        cursor.execute("DELETE FROM tblTemps WHERE city =" + keyfield)
##
##    for row in cursor.execute("SELECT * FROM tblTemps"):
##        print (row)
##
##deleteRec("cityTemperatures.db")
##
##input ("\nPress Enter to exit")
##



##conn = sqlite3.connect("CityTemperatures.db")
##cursor = conn.cursor()




##myRec = []
##city = input("\nEnter city name: ")
##while city != "xxx":
##    temperature = int(input ("Enter temperature: "))
##    localTime = input ("Enter local time: ")
##    myRec.append(city)
##    myRec.append(temperature)
##    myRec.append(localTime)
##    try:
##        cursor.execute("INSERT INTO tblTemps VALUES (?,?,?)", myRec)
##        conn.commit()
##    except:
##        print ("\nA record for this city already exists")
##    myRec=[]
##    city =input("\nEnter city name (xxx to end): ")
##conn.close()
##




##sql = """
##SELECT city, temperature
##FROM tblTemps
##WHERE temperature >= 25
##ORDER BY temperature DESC
##"""
##
##for row in cursor.execute(sql):
##    city, temperature = row
##    print(row)
##






##print("%-15s%20s%20s" %("City","Temperature","Local Time"))
######- = left align
######xs = how many spaces in the row
##for row in cursor.execute ('SELECT *FROM tblTemps ORDER BY temperature DESC LIMIT 5'):
##    city, temperature, localTime = row
##    print ("%-15s %15d %20s" % (city, temperature, localTime))
        




##for row in cursor.execute ('SELECT *FROM tblTemps ORDER BY temperature DESC'):
##    print(row)
##
##        
##
##cursor.execute("DROP TABLE IF EXISTS tblTemps")
##
##sqlCommand = """
##    CREATE TABLE tblTemps
##    (
##    city TEXT,
##    temperature INTEGER,
##    localTime TEXT,
##    primary key (city)
##    )"""
##
##cursor.execute(sqlCommand)
##
##tblTemps = [('London',7,'1200'),
##            ('Accra',30,'1200'),
##            ('Baghdad',20,'1500'),
##            ('Winnipeg',-12,'0600'),
##            ('New York',14,'0700'),
##            ('Nairobi',27,'1500'),
##            ('Sydney',22,'2300'),
##            ]
##
##
##cursor.executemany("INSERT INTO tblTemps VALUES (?,?,?)", tblTemps)
##
##conn.commit()
##conn.close()
##print("Table successfully created")


