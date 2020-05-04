import pandas
import numpy
import time

a = {
    "user_id": "1",
    "name": "Giana Shier",
    "email": "gshier0@4shared.com",
    "created_at": "2019-08-26 01:41:21",
    "last_login": "2019-09-22 02:15:32"
}
b = {
    "user_id": "2",
    "name": "Daniel Novak",
    "email": "novak@seznam.cz",
    "created_at": "2018-01-26 12:01:54",
    "last_login": "2019-09-21 06:35:12"
}

c = {
    "user_id": "3",
    "name": "Anne Shier",
    "email": "gshier0@gmail.com",
    "created_at": "2019-08-26 01:41:01",
    "last_login": "2019-09-22 02:15:23"
}
d = {
    "user_id": "4",
    "name": "Jan Novak",
    "email": "novak@email.cz",
    "created_at": "2018-03-26 12:01:19",
    "last_login": "2020-01-21 08:35:12"
}

e = {
    "user_id": "5",
    "name": "Giana Sherwood",
    "email": "gsr0@4shared.com",
    "created_at": "2019-08-26 12:41:21",
    "last_login": "2019-09-22 02:15:03"
}
f = {
    "user_id": "6",
    "name": "Daniel Novotny",
    "email": "novotny@seznam.cz",
    "created_at": "2020-01-26 10:01:32",
    "last_login": "2020-02-21 06:35:12"
}

g = {
    "user_id": "7",
    "name": "Giana Shier",
    "email": "gshier0@4shared.com",
    "created_at": "2019-08-26 01:41:21",
    "last_login": "2019-09-22 02:15:32"
}
h = {
    "user_id": "8",
    "name": "Daniel Novak",
    "email": "novak@seznam.cz",
    "created_at": "2018-01-26 12:01:54",
    "last_login": "2019-09-21 06:35:12"
}

j = {
    "user_id": "9",
    "name": "Jan Novak",
    "email": "novak@email.cz",
    "created_at": "2018-03-26 12:01:19",
    "last_login": "2020-01-21 08:35:12"
}

k = {
    "user_id": "10",
    "name": "Giana Sherwood",
    "email": "gsr0@4shared.com",
    "created_at": "2019-08-26 12:41:21",
    "last_login": "2019-09-22 02:15:03"
}
l = {
    "user_id": "11",
    "name": "Daniel Novotny",
    "email": "novotny@seznam.cz",
    "created_at": "2020-01-26 10:01:32",
    "last_login": "2020-02-21 06:35:12"
}

m = {
    "user_id": "12",
    "name": "Anne Shier",
    "email": "gshier0@gmail.com",
    "created_at": "2019-08-26 01:41:01",
    "last_login": "2019-09-22 02:15:23"
}

users_list = [a, b, c, d, e, f, g, h, j, k, l, m]

def return_all_users_data():
    return users_list

def return_user_data(user_id):
    for i in users_list:
        if i["user_id"] == user_id:
            return i
        else:
            pass