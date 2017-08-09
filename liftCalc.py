#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter
from collections import Counter
import sqlite3 as sql

lista = [{"weight": 10, "reps": 3},
         {"weight": 20, "reps": 4},
         {"weight": 30, "reps": 5},
         {"weight": 40, "reps": 6},
         {"weight": 50, "reps": 4},
         {"weight": 33, "reps": 6},
         {"weight": 12, "reps": 7},
         {"weight": 100, "reps": 9},
         {"weight": 105, "reps": 1},
         {"weight": 125, "reps": 2},
         {"weight": 120, "reps": 11},
         {"weight": 120, "reps": 12},
         {"weight": 120, "reps": 13},
         {"weight": 120, "reps": 14}]


def getAll():
    conn = sql.connect("records.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM lifts')
    for row in cur.fetchall():
        print(row)

def initLiftData(liftName):
    conn = sql.connect("records.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM lifts WHERE lift == ?;', [liftName])
    liftsTable = [dict(liftName=row[0],
                       weight=row[1],
                       reps=row[2],
                       estmax=row[3]) for row in cur.fetchall()]
    conn.close()
    return liftsTable


def addEntry(liftName, weight, reps):
    conn = sql.connect("records.db")
    cur = conn.cursor()
    cur.execute("""INSERT OR REPLACE INTO lifts (lift, weight, reps)
                   VALUES (?, ?, ?);""", [liftName, weight, reps])
    conn.commit()
    conn.close()

def newLift(liftName):
    conn = sql.connect("records.db")
    cur = conn.cursor()
    lista = []
    for reps in range(0,11):
        #dicce = {"liftname": liftName, "weight:":0, "reps": i, "estmax": 0}
        #lista.append(dicce)
        cur.execute('INSERT into lifts (lift, weight, reps) VALUES (?, ?, ?);', [liftName, 0, reps])
    conn.commit()
    conn.close()

        
def replace(liftName,weight, reps):
    def innerEpley(weight, reps):
        if reps == 1:
            return weight
        else:
            return weight * (1 + reps / float(30))
    estmax = innerEpley(weight,reps)

    conn = sql.connect("records.db")
    cur = conn.cursor()
    cur.execute("""UPDATE lifts 
                   SET weight == ?, estmax == ?
                   WHERE reps == ? AND lift == ?;""", [weight, estmax, reps, liftName])
    #cur.execute('INSERT OR REPLACE INTO lifts (lift, weight, reps) VALUES (?, ?, ?);', [liftName, weight, reps])
    

    [print(row) for row in cur.fetchall()]
    conn.commit()
    conn.close()


def EpleySort(dic):
    def innerEpley(weight, reps):
        if reps == 1:
            return weight
        else:
            return weight * (1 + reps / float(30))

    for row in dic:
        row["est1RM"] = innerEpley(row['weight'], row['reps'])
    sorted_list = sorted(dic, key=itemgetter('est1RM'), reverse=True)
    return sorted_list


def normalSort(dic):
    def innerEpley(weight, reps):
        if reps == 1:
            return weight
        else:
            return weight * (1 + reps / float(30))

    for row in dic:
        row["est1RM"] = innerEpley(row['weight'], row['reps'])
    sorted_list = sorted(dic, key=itemgetter('est1RM'), reverse=False)
    return sorted_list


def filterDuplicates(dic):
    k = [x['reps'] for x in dic]
    new_vals = []
    for i in Counter(k):
        all = [x for x in dic if x['reps'] == i]
        new_vals.append(max(all, key=lambda x: x['est1RM']))
    sorted_list = sorted(new_vals, key=itemgetter('est1RM'), reverse=True)
    return sorted_list  # [:9]  # ger bara tillbaka rep 1-9
