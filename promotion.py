# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:19:02 2020

@author: Roy
"""
import sqlite3
from sqlite3 import Error

def promotion_function(database1,database2):

    def get_tables(database):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        table = []
        try:
            cursor.execute("select * from SQLite_master")
            row = cursor.fetchall()
            rowlength = len(row)
            length = range(rowlength)
            for x in length:
                if ((x % 2) == 0):
                    table.append(row[x][1])
        except Error as e:
            table = [e]

        cursor.close()
        connection.close()
        return table
    table_list = get_tables(database1)

    sconn=sqlite3.connect(database2)
    empty_dictionary = {}
    cursor2 = sconn.cursor()
    loop = range(len(table_list))
    lo1 = len(table_list)
    print(loop)
    print(lo1)
    for x in table_list:
        comm_to_create="""create table if not exists {}(
                       rollno   text    primary key not null,
                       first   text    not null,
                       last   text    not null,
                       gr    text    not null,
                       gfn   text    not null,
                       sa    text    not null,
                       ay    text    not null,
                       std   text    not null,
                       branch    text    not null,
                       gpn   text    not null,
                       spn   text,
                       gea   text    not null,
                       sea   text,
                       s_cid     text,
                       g_cid     text)""".format(x)
        try:

            cursor2.execute(comm_to_create)

        except Error as e:
            print(e)


    for i in loop:
        empty_list = []
        fconn = sqlite3.connect(database1)
        cursor1 = fconn.cursor()
        comm_to_retrve = "select * from {}".format(table_list[i])
        cursor1.execute(comm_to_retrve)
        datarow = cursor1.fetchall()
        if(i<(lo1-1)):
            for element in datarow:
                print(element)
                try:

                    comm_to_insert = """insert into {0}(rollno,first,last,gr,gfn,sa,ay,std,branch,gpn,spn,gea,sea,s_cid,g_cid) values {1}""".format(table_list[i+1],element)
                    print(comm_to_insert)
                    cursor2.execute(comm_to_insert)
                    sconn.commit()
                    empty_list.append(element[0])
                except Error as e:
                    print(e)
                    sconn.rollback()

                empty_dictionary['{}'.format(table_list[i + 1])] = empty_list


        cursor1.close()
        fconn.close()

    return empty_dictionary
    cursor2.close()
    sconn.close()
        
