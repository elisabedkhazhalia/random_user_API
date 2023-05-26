import sys
import requests
import sqlite3
import json
from win10toast import ToastNotifier

api = 'https://randomuser.me/api/'
num_users = 5 

conn = sqlite3.connect('randomUser.sqlite3')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                gender TEXT,
                email TEXT,
                username TEXT,
                password TEXT);''')


for _ in range(num_users):
        response = requests.get(api)
        response.raise_for_status()  #  HTTP შეცდომების შემთხვევაში

        data = response.json()

        #  ვიღებთ შესაბამის ინფორმაციას API პასუხიდან 
        user = data['results'][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        gender = user['gender']
        email = user['email']
        username = user['login']['username']
        password = user['login']['password']

        cur.execute('''INSERT INTO users (name, gender, email, username, password)
                        VALUES (?, ?, ?, ?, ?)''', (name, gender, email, username, password))

        print(f"Inserted user: {name} ({gender})")
        print(f"Email: {email}")
        print(f"Username: {username}")
        print("")

        # შეტყობინების შექმნა
        toast = ToastNotifier()
        toast.show_toast("New User",
                         f"Name: {name}\nGender: {gender}\nEmail: {email}\nUsername: {username}",
                         duration=5)

conn.commit()
conn.close()

#  კოდის ეს ბლოკი პასუხისმგებელია API პასუხიდან მიღებული მონაცემების ჩაწერაზე JSON ფაილში სახელად "data.json" .
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


