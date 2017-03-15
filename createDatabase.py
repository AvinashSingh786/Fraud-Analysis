import sqlite3
from elizabeth import Personal
from random import randint, uniform
from faker import Faker

'''
    Globals
'''
m_status = ("Married", "Single", "Never Married", "Divorced")
c_loss = ("Fire", "Water", "Theft")
f_loss = ("No Fire", "No Water", "No Theft")
i_insurer = ("Santam", "Hollard", "Outsurance", "Discovery", "Absa", "Mutual & Federal", "First for Woman", "Budget", "Miway")

person = Personal('en')
fake = Faker()

'''
    Functions
'''


def create_database():
    conn = sqlite3.connect('insurance.db')
    cur = conn.cursor()
    print("Opened database successfully")

    cur.execute('''CREATE TABLE IF NOT EXISTS Claims
           (Claim_ID                INT PRIMARY KEY  AUTOINCREMENT NOT NULL,
           Name                     TEXT,
           Surname                  TEXT,
           Age                      INTEGER,
           Gender                   VARCHAR(8),
           Marital_Status           TEXT,
           Date_Of_Birth            DATE,
           Sum_Insured              REAL,
           Policies_Revenue         REAL,
           Policy_Start             DATE,
           Policy_End               DATE,
           Fraudulent_Claim         VARCHAR(1),
           Fraudulent_Claim_Reason  TEXT,
           Date_Of_Loss             DATE,
           Date_Of_Claim            DATE,
           Broker_ID                TEXT,
           Insured_ID               TEXT,
           Kind_Of_Loss             TEXT,
           Claim_Amount             REAL,
           Party_Name               TEXT,
           Party_Surname            TEXT,
           Service_Provider         TEXT,
           Policy_Holder_Street     TEXT,
           Policy_Holder_Province   TEXT,
           Policy_Holder_City       TEXT,
           Policy_Holder_Area       TEXT,
           Policy_Holder_Postal     TEXT,
           Province                 TEXT,
           City                     TEXT,
           Area                     TEXT,
           Postal_Code              TEXT);''')
    print("Created Database table successfully!")

    for i in range(0, 10):
        cur.execute("INSERT INTO Claims VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", get_data())
    conn.commit()
    conn.close()


def get_data():
    return (
        person.name(),
        person.surname(),
        person.age(),
        person.gender(),
        marital_status(),
        date("-80y", "-18y"),
        random_real(0, 2000000),
        random_real(0, 20000),
        date("-80y", "now"),
        date("-80y", "now"),
        "F", "REASON",
        date("-80y", "now"),
        date("-80y", "now"),
        "BKR"+randint(1000, 9999), i_insurer[randint(0, len(i_insurer))],
        c_loss[randint(0, len(c_loss))],
        random_real(0, 70000),
        person.name(),
        person.surname(),
        fake.company(),
        fake.street(),
        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode(),

        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode()
    )


def marital_status():
    return m_status[randint(0, len(m_status))]


def date(start, end):
    fake.date_time_between(start, end, tzinfo=None)


def random_real(m, mm):
    return round(uniform(m, mm), 2)


print(get_data())

'''
    Data Cleaning
        - Check if DOB and age is correct
        - check claim date
        - policy expire
        - amount claim vs insured
'''


