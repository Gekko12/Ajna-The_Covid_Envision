"""
Backend file used for DataBase
"""

import sqlite3 as sq


class DBInitialization:
    """
        Initialization class used to initialize the whole DB.
            Variable -
                fname : file name of DataBase file.
                con : connect to the database file.
                cur : cursor used to execute SQL cmds.
            Functions -
                dropTables() : to drop all tables except Zonal table
                zonalReset(zfile) : reset Zonal data and re-fill all the data from zfile.txt
                createTables() : to create all the tables
                helplineNum(helpfile) : reset covid helpline numbers and re-fill all the data from helpfile

    """
    fname = ""
    con = ""
    cur = ""

    def __init__(self, filename):
        self.fname = filename
        self.con = sq.connect(filename)
        self.cur = self.con.cursor()

    def dropTables(self):
        """
        Drop(delete) all tables from database.
        :return: returns 0 if all goes well else print error msg and return -1
        """
        try:
            self.cur.execute('''
                DROP TABLE IF EXISTS "Student" ''')
            self.cur.execute('''
                DROP TABLE IF EXISTS "Travel History" ''')
            self.cur.execute('''
                DROP TABLE IF EXISTS "Covid Symptoms" ''')
            self.cur.execute('''
                DROP TABLE IF EXISTS "Meet History" ''')
            self.cur.execute('''
                DROP TABLE IF EXISTS "Covid HelpLine Numbers" ''')
            self.con.commit()
            return 0
        except Exception as e:
            print("dropTables() error -", e)
            self.con.close()
            return -1

    def zonalReset(self, zfile):
        """
        reset Zonal data and re-fill all the data from zfile.txt
        :param zfile: file name which contains zonal data
        :return: returns 0 if all goes well else print error msg and return -1
        """
        try:
            fh = open(zfile)
            patt = ' | '
            self.cur.execute('''
                DROP TABLE IF EXISTS "Zonal" ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Zonal" (
                "State"	TEXT NOT NULL,
                "District" TEXT NOT NULL,
                "Zone"	TEXT NOT NULL,
                PRIMARY KEY("District")
                ) ''')

            for line in fh:
                if len(line) < 1:
                    continue
                data = line.strip().split(patt)
                # print(data)
                self.cur.execute('''
                    INSERT INTO "Zonal" VALUES(?, ?, ?)
                        ''', (data[0], data[1], data[2],))
            fh.close()
            self.con.commit()
        except Exception as e:
            print("zonalReset() error - ", e)
            self.con.close()
            return -1

    def createTables(self):
        """
            It creates all the tables required for that project
            :return : returns 0 if all goes well else error msg with return status -1
        """
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Student"(
                "SName"	TEXT NOT NULL,
                "USN"	TEXT NOT NULL UNIQUE,
                "UserName" TEXT NOT NULL UNIQUE,
                "Phone Number"	INTEGER NOT NULL UNIQUE,
                "Password" TEXT NOT NULL,
                "Reset_Scheduled" TEXT NULL,
                PRIMARY KEY("USN", "UserName")
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Zonal" (
                "State"	TEXT NOT NULL,
                "District" TEXT NOT NULL,
                "Zone"	TEXT NOT NULL,
                PRIMARY KEY("District")
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Travel History"(
                "USN" TEXT NOT NULL,
                "Date" TEXT, 
                "State" TEXT,
                "District" TEXT NOT NULL,
                FOREIGN KEY("District") REFERENCES "Zonal"("District"),
                FOREIGN KEY("USN") REFERENCES "Student"("USN")
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Covid Symptoms"(
                "USN" TEXT NOT NULL,
                "Cough" BOOLEAN NOT NULL CHECK ("Cough" IN (0,1)) ,
                "Fever" BOOLEAN NOT NULL CHECK ("Fever" IN (0,1)) ,
                "Breathlessness" BOOLEAN NOT NULL CHECK ("Breathlessness" IN (0,1)) ,
                "Loss of Taste/Smell" BOOLEAN NOT NULL CHECK ("Loss of Taste/Smell" IN (0,1)) ,
                "Interacted with Covid +ve" BOOLEAN NOT NULL CHECK ("Interacted with Covid +ve" IN (0,1)) ,
                "Healthcare interact positive" BOOLEAN NOT NULL CHECK ("Healthcare interact positive" IN (0,1)) ,
                "Covid Positive" BOOLEAN NOT NULL CHECK ("Covid Positive" IN (0,1)) ,
                "Color" TEXT NOT NULL,
                FOREIGN KEY("USN") REFERENCES "Student"("USN") ON DELETE CASCADE ,
                PRIMARY KEY ("USN")
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Meet History" (
                "USN"	TEXT NOT NULL,
                "Date"	TEXT NOT NULL,
                "M_USN" TEXT NOT NULL,
                "M_Name" TEXT,
                FOREIGN KEY("USN") REFERENCES "Student"("USN") ON DELETE CASCADE
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Covid HelpLine Numbers" (
                "State"	TEXT NOT NULL,
                "HelpLine Nos."	TEXT NOT NULL
                ) ''')
            self.con.commit()
            return 0
        except Exception as e:
            print("createTables() error - ", e)
            self.con.close()
            return -1

    def helplineNum(self, helpfile):
        """
        reset covid helpline numbers and re-fill all the data from helpfile
        :param helpfile: file which contains the covid helpline Numbers
        :return : returns 0 if all goes well else print error msg and return -1
        """
        try:
            fh = open(helpfile)
            patt = ' | '
            anoum = ', '
            self.cur.execute('''
                DROP TABLE IF EXISTS "Covid HelpLine Numbers" ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Covid HelpLine Numbers" (
                "State"	TEXT NOT NULL,
                "HelpLine Nos."	TEXT NOT NULL
                ) ''')

            for line in fh:
                if len(line) < 2:
                    continue
                data = line.strip().split(patt)
                # print(data)
                # if more than one number exists
                if data[1].find(anoum) != -1:
                    lst_num = data[1].strip().split(anoum)
                    for num in lst_num:
                        self.cur.execute('''
                            INSERT INTO "Covid HelpLine Numbers" VALUES(?, ?)
                            ''', (data[0], num,))
                else:
                    self.cur.execute('''
                    INSERT INTO "Covid HelpLine Numbers" VALUES(?, ?)
                    ''', (data[0], data[1],))

            self.con.commit()
            return 0
        except Exception as e:
            print("helplineNum() error - ", e)
            self.con.close()
            return -1

    def __del__(self):
        # destructor of the class
        self.con.close()


class DBInsertion:
    """"
    This class used to insert Data into DB
    Functions-
        1.studentInsertion(name, usn, username, phone, password)
        2.
    """

    def __init__(self, filename):
        self.fname = filename
        self.con = sq.connect(filename)
        self.cur = self.con.cursor()

    def studentInsertion(self, name, usn, username, phone, password):
        """
        This function insert data into Student table
        :param name:
        :param usn:
        :param username:
        :param phone:
        :param password:
        :return: returns 0 if all goes well else print error msg and return -1 and response msg
        """
        try:
            self.cur.execute('''
            INSERT INTO Student(SName, USN, UserName, "Phone Number", Password) 
            VALUES(?, ?, ?, ?, ?)''', (name, usn, username, phone, password,))
            self.con.commit()
            return [0, "Everything is fine"]
        except Exception as e:
            print("studentInsertion() error -", e)
            res = e
            self.con.close()
            return [-1, res]

    def setphoneNoasPwd(self, username):
        """
        This will change the password of user(using username) to phone number
        :param username:
        :return: returns 0 if everything fine else -1
        """
        try:
            self.cur.execute('''
            UPDATE "Student"
            SET "Password" = (SELECT "Phone Number"
                                FROM "Student"
                                WHERE "UserName" = ?)
            WHERE "UserName" = ?''', (username, username,))
            self.con.commit()
            return 0
        except Exception as e:
            print("setphoneNoasPwd():, error -", e)
            self.con.close()
            return -1

    def resetScheduledDate(self, username, date, mode="normal"):
        """
        This will enter the Reset_Scheduled ie. date(15 days later) after opting for reset
        :param username: user's name
        :param date: date after opted for reset
        :param mode: if user forced to delete than mode is forced else normal
        :return: returns 0 if everything fine else -1 and if already exist the date will be passed
        """
        try:
            self.cur.execute('''SELECT * FROM Student WHERE UserName = ?''', (username,))
            rows = self.cur.fetchall()
            # print(rows)
            if len(rows) != 0:
                if mode == "forced":
                    self.cur.execute('''
                    UPDATE Student
                    SET Reset_Scheduled = ?
                    WHERE UserName = ? ''', (date, username,))
                    self.con.commit()
                    return ["Done", 0]
                elif rows[0][5] is None:  # as None means NULL in DB
                    self.cur.execute('''
                    UPDATE Student
                    SET Reset_Scheduled = ?
                    WHERE UserName = ? ''', (date, username,))
                    self.con.commit()
                    return ["Done", 0]  # 0 means resetted first time
                else:
                    return ["Already - Resetted", rows[0][5]]
        except Exception as e:
            print("resetScheduledDate() error -", e)
            self.con.close()
            return ["Error", -1]

    def meetTravelHistInsert(self, state_t, distr_t, date_t, date_m, name_m, usn_m, usn):
        """
        This function inserts data into Meet History and Travel History table
        :param state_t:
        :param distr_t:
        :param date_t:
        :param date_m:
        :param name_m:
        :param usn_m:
        :param usn:
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Travel History"
            WHERE USN=? AND Date=? AND State=? AND District=?''', (usn, date_t, state_t, distr_t,))
            row_t = self.cur.fetchall()
            if len(row_t) != 0:
                if row_t[0][0] == usn and row_t[0][1] == date_t and row_t[0][2] == state_t and row_t[0][3] == distr_t:
                    pass
            else:
                self.cur.execute('''
                INSERT INTO "Travel History" VALUES (?, ?, ?, ?)''', (usn, date_t, state_t, distr_t,))
                self.con.commit()

            self.cur.execute('''
            SELECT * FROM "Meet History"
            WHERE USN=? AND Date=? AND "M_USN"=? AND "M_Name"=?''', (usn, date_m, usn_m, name_m,))
            row_m = self.cur.fetchall()
            if len(row_m) != 0:
                if row_m[0][0] == usn and row_m[0][1] == date_m and row_m[0][2] == usn_m and row_m[0][3] == name_m:
                    return 0, "Data Already exist"
            else:
                # print("DB-->", usn, date_m, usn_m, name_m)
                self.cur.execute('''
                INSERT INTO "Meet History" VALUES (?, ?, ?, ?)''', (usn, date_m, usn_m, name_m,))
            self.con.commit()
            return 0, "Done"
        except Exception as e:
            print("meetTravelHistInsert(), error -", e)
            self.con.close()
            return -1

    def covidSympInsertion(self, usn, cough, fever, breathless, loss_taste, interaction, healthcare, covid_positive, color):
        """
        This function inserts data into Covid Symptoms Table
        :param usn:
        :param cough:
        :param fever:
        :param breathless:
        :param loss_taste:
        :param interaction:
        :param healthcare:
        :param covid_positive:
        :param color:
        :return: returns 0 if everything is fine else -1
        """
        try:
            self.cur.execute('''SELECT * FROM "Covid Symptoms" WHERE USN=? ''', (usn,))
            row = self.cur.fetchall()

            if len(row) == 0:
                self.cur.execute('''
                INSERT INTO "Covid Symptoms" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                 (usn, cough, fever, breathless, loss_taste, interaction, healthcare, covid_positive, color,))
            else:
                self.cur.execute('''
                UPDATE "Covid Symptoms"
                SET "Cough"=?, "Fever"=?, "Breathlessness"=?, "Loss of Taste/Smell"=?, "Interacted with Covid +ve"=?,
                "Healthcare interact positive"=?, "Covid Positive"=?, "Color"=?
                WHERE USN=? ''', (cough, fever, breathless, loss_taste, interaction, healthcare, covid_positive, color, usn,))

            self.con.commit()
            return 0
        except Exception as e:
            print("covidSympInsertion(), error -", e)
            self.con.close()
            return -1

    def __del__(self):
        # destructor of the class
        self.con.close()


class DBsearch:
    """
    This class facilates search
    """

    def __init__(self, filename):
        self.fname = filename
        self.con = sq.connect(filename)
        self.cur = self.con.cursor()

    def userSearch(self, username, pwd="abc", usneed=False):
        """
        Checks whether username or pwd related to each other
        :param username:
        :param pwd:
        :param usneed: to get the usn of user using username
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Student"
            WHERE "UserName" = ?''', (username,))

            rows = self.cur.fetchall()
            # print(rows)
            if usneed:
                return rows[0][1]
            elif len(rows) == 0:
                return "Empty"  # if no account yet created or wrong username
            elif len(rows) == 1 and rows[0][4] == pwd:
                return True
            return False  # if wrong password inserted
        except Exception as e:
            print("userSearch(), error -", e)
            self.con.close()
            return -1

    def travelSearch(self, usn):
        """
        This functions returns the search values
        :param: usn
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Travel History" WHERE USN=?''', (usn, ))
            rows = self.cur.fetchall()
            return rows
        except Exception as e:
            print("travelSearch(), error -", e)
            self.con.close()
            return -1

    def meetSearch(self, usn):
        """
        This functions returns the search values
        :param: usn
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Meet History" WHERE USN=?''', (usn, ))
            rows = self.cur.fetchall()
            self.con.commit()
            return rows
        except Exception as e:
            print("meetSearch(), error -", e)
            self.con.close()
            return -1

    def colorSearch(self, usn):
        """
        This will result the color ie. green, red, orange according to user's covid status
        :param usn:
        :return: returns color else green color by default
        """
        try:
            self.cur.execute('''
            SELECT Color FROM "Covid Symptoms" WHERE USN=? ''', (usn,))
            color = self.cur.fetchall()
            if len(color) != 0:
                return color
            else:
                return "green"
        except Exception as e:
            print("colorSearch(), error -", e)
            self.con.close()
            return -1

    def infectionSearch(self, usn):
        """
        This function gives the information of meeting for suspicious and covid positive users
        :param usn:
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Meet History" WHERE USN=? ''', (usn,))
            meets = self.cur.fetchall()
            # print(meets)
            if len(meets) == 0:
                return "Empty - no record found !!!"

            self.cur.execute('''
            SELECT USN, Color FROM "Covid Symptoms" WHERE (Color="orange" OR Color="red")
             AND NOT USN=?''', (usn,))
            users = self.cur.fetchall()
            # print(users)

            res_lst = []
            status = "Suspicious"
            for user in users:
                for x in meets:
                    if x[2] == user[0]:
                        if user[1] == "red":
                            status = "Covid Positive"
                        res_lst.append((x[1], x[2], x[3], status))
            return res_lst
        except Exception as e:
            print("infectionSearch(), error -", e)
            return -1

    def __del__(self):
        # destructor of the class
        self.con.close()


class DBDeletion:
    """
    This class used to delete database
    """

    def __init__(self, filename):
        self.fname = filename
        self.con = sq.connect(filename)
        self.cur = self.con.cursor()

    def meetTravelHistDel(self, usn):
        """
        This function deletes the Meet and Travel History of user
        :param usn:
        :return: returns 0 and a msg if everything goes well , else -1
        """
        try:
            self.cur.execute('''
            DELETE FROM "Meet History"
            WHERE USN = ?''', (usn,))
            self.cur.execute('''
            DELETE FROM "Travel History"
            WHERE USN = ?''', (usn,))
            self.con.commit()
            return 0, "Meet and Travel History of " + usn + " DELETED"
        except Exception as e:
            print("meetTravelHistDel(), error -", e)
            self.con.close()
            return -1

    def __del__(self):
        # destructor of the class
        self.con.close()


'''
# main-function
obj = DBInitialization('backgrounds/Ajna.db')
obj.dropTables()
obj.zonalReset('backgrounds/ZonalDataFinal.txt')
'''
'''
obj = DBInitialization('backgrounds/Ajna.db')
obj.createTables()
obj.helplineNum('backgrounds/CovidHelpLineNo.txt')
#'''
'''
obj1 = DBsearch('backgrounds/Ajna.db')
print(obj1.infectionSearch('1AT18CS128'))
#print(obj1.userSearch("Gekko", "mypwd1"))
#'''
'''
obj2 = DBInsertion('backgrounds/Ajna.db')
print(obj2.covidSympInsertion('1AT18CS128',1,0,0,0,0,0,0,"GREEN"))
#'''
'''
obj3 = DBDeletion('backgrounds/Ajna.db')
#print(obj3.meetTravelHistDel('1AT18CS128'))
#'''
