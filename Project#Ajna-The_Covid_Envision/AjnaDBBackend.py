"""
Backend file used for DataBase
"""

import sqlite3 as sq


class Initialization:
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
            print(e)
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
            print(e)
            self.con.close()
            return -1

    def createTables(self):
        """
            It creates all the tables required for that project
            :return : returns 0 if all goes well else error msg with return status -1
        """
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "Student"(
                "USN"	TEXT NOT NULL,
                "SName"	TEXT NOT NULL,
                "Address"	TEXT,
                "Phone Number"	INTEGER NOT NULL UNIQUE,
                "Gender"	TEXT,
                PRIMARY KEY("USN")
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
            print(e)
            self.con.close()
            return -1

    def __del__(self):
        # destructor of the class
        self.con.close()


# main-function
obj = Initialization('Ajna.db')
obj.dropTables()
obj.zonalReset('ZonalDataFinal.txt')
obj.createTables()
