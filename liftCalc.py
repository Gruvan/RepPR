from operator import itemgetter
from collections import Counter
import sqlite3 as sql

lista = [{"weight": 10, "reps": 3},
         {"weight": 20, "reps": 4},
         {"weight": 30, "reps": 5},
         {"weight": 40, "reps": 6},
         {"weight": 50, "reps": 4},
         {"weight": 33, "reps": 6},
         {"weight": 12, "reps": 6},
         {"weight": 100, "reps": 9},
         {"weight": 133, "reps": 7}]


conn = sql.connect("records.db")
cur = conn.cursor()


def initLiftData():
    conn = sql.connect("records.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Bench')
    for row in cur.fetchall():
        print(row)


def addEntry(weight, reps):
    # if reps > 10:
    # break
    pass


def EpleyAndSort(dic):
    def innerEpley(weight, reps):
        max = weight * (1 + reps / float(30))
        return max
    for row in dic:
        row["est1RM"] = innerEpley(row['weight'], row['reps'])
    sorted_list = sorted(dic, key=itemgetter('est1RM'), reverse=True)
    return sorted_list


def filterDuplicates(dic):
    k = [x['reps'] for x in dic]
    new_vals = []
    for i in Counter(k):
        all = [x for x in dic if x['reps'] == i]
        new_vals.append(max(all, key=lambda x: x['est1RM']))
    sorted_list = sorted(new_vals, key=itemgetter('est1RM'), reverse=True)
    return sorted_list
