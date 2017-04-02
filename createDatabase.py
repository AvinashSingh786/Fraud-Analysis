import sqlite3
from elizabeth import Personal
from random import randint, uniform
from faker import Faker
from datetime import date, datetime
from sys import stdout
import pickle
import calendar
import time

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

mindate = datetime.strptime('Jun 1 1900  1:33PM', '%b %d %Y %I:%M%p')
maxdate = datetime.today()


'''
    Functions
'''


'''
    :param n - number of claims to insert
    :param f - number of fraud claims
'''


def create_database(n, f):
    fraud = set([int(randint(0, n)) for i in range(f)])
    print(fraud)
    pickle.dump(fraud, open("fraud-pickle.txt", "wb"))
    text_file = open("fraud-index.txt", "w")
    text_file.write("%s" % ', '.join(str(e) for e in fraud))
    text_file.close()

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
        if i not in fraud:
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

'''
    :param status - sends the function to generate a fraud claim or valid claim
'''


def get_data(status):
    dob = random_date()
    dateloss = rand_date("-40y", "now")
    policystart = rand_date("-40y", "now")
    suminsured = random_real(200000, 10000000)

    dobiso = dob.isoformat()
    policystartiso = policystart.isoformat()
    datelossiso = dateloss.isoformat()

    if not status:
        return get_fraud_data()

    return (
        null_val(),
        person.name(),
        person.surname(),
        calculate_age(dob, status),
        person.gender(),
        marital_status(),
        dobiso,
        suminsured,
        random_real(100, 5000),
        policystartiso,
        policy_end(policystart, True),
        "F", "",
        datelossiso,
        date_claim(dateloss, True),
        "BKR" + str(randint(1000, 9999)), i_insurer[randint(0, len(i_insurer) - 1)],
        c_loss[randint(0, len(c_loss) - 1)],
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

'''
    function to generate fake data based on the status - False to the helper functions
'''


def get_fraud_data():
    dob = random_date()
    dateloss = rand_date("-40y", "now")
    policystart = rand_date("-40y", "now")
    suminsured = random_real(200000, 10000000)
    r = randint(1, 9)
    dobiso = dob.isoformat()
    policystartiso = policystart.isoformat()
    datelossiso = dateloss.isoformat()

    if r == 1:
        dob = ""
        dobiso = ""

    if r == 4:
        policystart = ""
        policystartiso = ""

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
        policystartiso,
        policy_end(policystart, r),
        "T", fraud_reasons[r - 1],
        datelossiso,
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
    if loss == "":
        return ""
    if s == 7:
        return date_between(mindate, loss).isoformat()
    return date_between(loss, maxdate).isoformat()


def policy_end(start, s):
    if start == "":
        return ""
    if s == 6:
        return date_between(mindate, start).isoformat()
    if s == 5:
        return ""
    return date_between(start, maxdate).isoformat()


def date_between(s, e):
    y = randint(s.year, e.year)
    m = randint(1, 12)
    d = randint(1, 30)

    if calendar.isleap(y):
        if m == 2:
            d = randint(1, 29)

    if m == 2:
        d = randint(1, 28)

    h = randint(0, 12)
    i = randint(0, 59)
    s = randint(0, 59)

    return datetime(y, m, d, h, i, s)


def claim_amount(val, s):
    if s == 3:
        return random_real(val, 5000000)
    return random_real(1, val)


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
    return m_status[randint(0, len(m_status) - 1)]


def random_date():
    y = randint(1920, 1999)
    m = randint(1, 12)
    d = randint(1, 30)
    if calendar.isleap(y):
        if m == 2:
            d = randint(1, 29)

    if m == 2:
        d = randint(1, 28)

    h = randint(0, 12)
    i = randint(0, 59)
    s = randint(0, 59)

    return datetime(y, m, d, h, i, s)


def rand_date(start, end):
    return fake.date_time_between(start, end)


def random_real(m, mm):
    return round(uniform(m, mm), 2)


def null_val():
    return None


'''
    SCRIPT
    
    eg. create_database(number of claims, number of fraud claims)
'''

start_time = time.time()
create_database(100000, 175)
print("--- %s seconds ---" % (time.time() - start_time))

'''
    Data Cleaning
        - Check if DOB and age is correct
        - check claim date
        - policy expire
        - amount claim vs insured
'''
