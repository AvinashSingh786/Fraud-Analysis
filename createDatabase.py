import sqlite3
from elizabeth import Personal
from random import randint, uniform
from faker import Faker
from datetime import date
from sys import stdout
import pickle

'''
    Globals
'''
m_status = ("Married", "Single", "Divorced", "Widowed", "Separated")
c_loss = ("Fire", "Water", "Theft", "Natural Disaster")
n_loss = ("Borrowed", "Misplaced", "Donated")
i_insurer = ("Santam", "Hollard", "Outsurance", "Discovery", "Absa", "Mutual & Federal", "First for Woman", "Budget",
             "Miway")
fraud_reasons = ("No Date of birth", "Date of birth and Age do not match", "Claim amount is more than Sum Insured",
                 "No Policy start date", "No Policy end date", "Policy end date before start date",
                 "Claim Date before loss", "No kind of loss", "Invalid kind of loss")
person = Personal('en')
fake = Faker()

'''
    Functions
'''


def create_database(n, f):
    fraud = set([int(randint(0, n)) for i in range(f)])
    print(fraud)
    pickle.dump(fraud, open("fraud-index.txt", "wb"))
    conn = sqlite3.connect('insurance.db')
    cur = conn.cursor()
    print("Opened database successfully")

    cur.execute('''CREATE TABLE IF NOT EXISTS Claims
           (Claim_ID                INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
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

    for i in range(0, n):
        if n not in fraud:
            cur.execute("INSERT INTO Claims VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        get_data(True))
            print("\rInserted: " + str(i), end="")
        else:
            cur.execute("INSERT INTO Claims VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        get_data(False))
            print("\rInserted: " + str(i), end="")
    conn.commit()
    conn.close()

    print("\nAll data inserted successfully")


def get_data(status):
    dob = fake.date_time(tzinfo=None)
    dateloss = rand_date("-40y", "now")
    policystart = rand_date("-40y", "now")
    suminsured = random_real(200000, 10000000)
    if not status:
        return get_fraud_data()

    return (
        null_val(),
        person.name(),
        person.surname(),
        calculate_age(dob, status),
        person.gender(),
        marital_status(),
        dob.isoformat(),
        suminsured,
        random_real(100, 5000),
        policystart,
        policy_end(policystart, True),
        "F", "",
        dateloss,
        date_claim(dateloss, True),
        "BKR"+str(randint(1000, 9999)), i_insurer[randint(0, len(i_insurer)-1)],
        c_loss[randint(0, len(c_loss)-1)],
        claim_amount(suminsured, True),
        person.name(),
        person.surname(),
        fake.company(),
        fake.street_name(),
        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode(),

        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode()
    )


def get_fraud_data():
    dob = fake.date_time(tzinfo=None)
    dateloss = rand_date("-40y", "now")
    policystart = rand_date("-40y", "now")
    suminsured = random_real(200000, 10000000)
    r = randint(1, 9)
    dobiso = dob.isoformat()

    if r == 1:
        dob = ""
        dobiso = ""
    if r == 4:
        policystart = ""

    return (
        null_val(),
        person.name(),
        person.surname(),
        calculate_age(dob, r),
        person.gender(),
        marital_status(),
        dobiso,
        suminsured,
        random_real(100, 5000),
        policystart,
        policy_end(policystart, r),
        "T", fraud_reasons[r-1],
        dateloss,
        date_claim(dateloss, r),
        "BKR" + str(randint(1000, 9999)), i_insurer[randint(0, len(i_insurer) - 1)],
        c_loss[randint(0, len(c_loss) - 1)],
        claim_amount(suminsured, r),
        person.name(),
        person.surname(),
        fake.company(),
        fake.street_name(),
        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode(),

        fake.country(),
        fake.city(),
        fake.state(),
        fake.postalcode()
    )


def kind_loss(s):
    if s == 8:
        return ""
    if s == 9:
        return n_loss[randint(0, len(c_loss) - 1)]
    return c_loss[randint(0, len(c_loss) - 1)]


def date_claim(loss, s):
    if s == 7:
        return fake.date_time_between("", loss).isoformat()
    return fake.date_time_between(loss, "now").isoformat()


def claim_amount(val, s):
    if s == 3:
        return random_real(val, 5000000)
    return random_real(1, val)


def policy_end(start, s):
    if s == 6:
        return fake.date_time_between("", start).isoformat()
    if s == 5:
        return ""
    return fake.date_time_between(start, "now").isoformat()


def calculate_age(born, s):
    if s == 2:
        return person.age()
    if s == 4:
        return person.age()
    if born == "":
        return ""
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def marital_status():
    return m_status[randint(0, len(m_status)-1)]


def rand_date(start, end):
    # return fake.date_time_between(start, end).isoformat()
    return fake.date_time(tzinfo=None).isoformat()


def random_real(m, mm):
    return round(uniform(m, mm), 2)


def null_val():
    return None
'''
    SCRIPT

'''
# create_database(10, 2)
for i in range(0,100):
    print(get_data(True))
    print(get_fraud_data())
'''
    Data Cleaning
        - Check if DOB and age is correct
        - check claim date
        - policy expire
        - amount claim vs insured
'''


