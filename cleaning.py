import sqlite3


def clean_data():
    conn = sqlite3.connect('insurance.db')
    cur = conn.cursor()
    print("Opened database successfully")

    cur.execute('''''')
    print("Created Database table successfully!")

    conn.commit()
    conn.close()
    return ""

"""
    SCRIPT
"""
clean_data()
