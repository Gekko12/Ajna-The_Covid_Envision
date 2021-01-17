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
                "Reset_Scheduled" TEXT,
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
                "State" TEXT,
                "District" TEXT NOT NULL,
                FOREIGN KEY("District") REFERENCES "Zonal"("District"),
                FOREIGN KEY("USN") REFERENCES "Student"("USN")
                ) ''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Covid Symptoms"(
                "USN" TEXT NOT NULL,
                "Covid Positive" BOOLEAN NOT NULL CHECK ("Covid Positive" IN (0,1)) ,
                "Fever" BOOLEAN NOT NULL CHECK ("Fever" IN (0,1)) ,
                "Cough" BOOLEAN NOT NULL CHECK ("Cough" IN (0,1)) ,
                "Breathlessness" BOOLEAN NOT NULL CHECK ("Breathlessness" IN (0,1)) ,
                "Body Ache" BOOLEAN NOT NULL CHECK ("Body Ache" IN (0,1)) ,
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
            WHERE "UserName" = ?''', (username, username, ))
            self.con.commit()
            return 0
        except Exception as e:
            print("setphoneNoasPwd():, error -", e)
            self.con.close()
            return -1

    def resetScheduledDate(self, username, date):
        """
        This will enter the Reset_Scheduled ie. date(15 days later) after opting for reset
        :param username: user's name
        :param date: date after opted for reset
        :return: returns 0 if everything fine else -1
        """
        try:
            # insert into [table] (data) Values
            #               ((CASE WHEN @d IS NULL OR datalength(@d) = 0 THEN NULL ELSE @d END))
            self.cur.execute('''
            INSERT INTO Student(Reset_Scheduled) VALUES(
            (CASE WHEN Reset_Scheduled IS NULL THEN )
            WHERE ''', (date,))
            self.con.commit()
            return 0
        except Exception as e:
            print("resetScheduledDate() error -", e)
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

    def userSearch(self, username, pwd="abc"):
        """
        Checks whether username or pwd related to each other
        :param username:
        :param pwd:
        :return:
        """
        try:
            self.cur.execute('''
            SELECT * FROM "Student"
            WHERE "UserName" = ?''', (username,))

            rows = self.cur.fetchall()
            # print(rows)
            if len(rows) == 0:
                return "Empty"      # if no account yet created or wrong username
            elif len(rows) == 1 and rows[0][4] == pwd:
                return True
            return False        # if wrong password inserted
        except Exception as e:
            print("userSearch(), error -", e)
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
obj.createTables()
obj.helplineNum('backgrounds/CovidHelpLineNo.txt')
#'''
'''
obj1 = DBsearch('backgrounds/Ajna.db')
print(obj1.userSearch("Gekko", "mypwd1"))
#'''
'''
obj2 = DBInsertion('backgrounds/Ajna.db')
obj2.setphoneNoasPwd(username)
'''
