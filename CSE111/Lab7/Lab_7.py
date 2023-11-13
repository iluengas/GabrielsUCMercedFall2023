import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try: 
        sql = """CREATE TABLE warehouse(
                    w_warehousekey decimal (9,0) not null,
                    w_name char(100) not null,
                    w_capacity decimal(6,0) not null,
                    w_suppkey decimal(9,0) not null,
                    w_nationkey decimal(2,0) not null)"""
        _conn.execute(sql)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try: 
        sql = "DROP TABLE warehouse"
        _conn.execute(sql)

        _conn.commit()
    except Error as e: 
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")


    try:
        count = 0
        q1 = """SELECT s_suppkey, n_name, s_nationkey, s_name
                FROM supplier, nation
                WHERE s_nationkey = n_nationkey""" 
        cur = _conn.cursor()
        cur.execute(q1)
        rows1 = cur.fetchall()

        q2 = """SELECT s_nationkey, MAX(sum)
                FROM (
                    SELECT ps_suppkey, s_nationkey , SUM(p_size) as sum
                    FROM part, partsupp, supplier
                    WHERE p_partkey = ps_partkey AND 
                            ps_suppkey = s_suppkey
                                GROUP BY ps_suppkey
                )
                    GROUP BY s_nationkey""" 
        cur = _conn.cursor()
        cur.execute(q2)
        rows2 = cur.fetchall()        

        temp = None

        for row in rows1:
            name = row[3] + "___" + row[1]
            count += 1
            for row2 in rows2:
                if row2[0] == row[2]:
                    temp = row2[1]*3
            insertIntoWarehouse(_conn,count,row[0],temp,name,row[2]) 
            count += 1
            for row2 in rows2:
                if row2[0] == row[2]:
                    temp = row2[1]*3
            insertIntoWarehouse(_conn,count,row[0],temp,name,row[2]) 
            count += 1
            for row2 in rows2:
                if row2[0] == row[2]:
                    temp = row2[1]*3
            insertIntoWarehouse(_conn,count,row[0],temp,name,row[2])  
    except Error: 
        _conn.rollback()
        print(Error)



    print("++++++++++++++++++++++++++++++++++")

def insertIntoWarehouse(_conn, _count, _suppkey, _capacity, _nationname, _nationkey):
    try:
        sql = """INSERT INTO warehouse(w_warehousekey,
                    w_name, w_capacity, w_suppkey, w_nationkey)
                    VALUES(?, ?, ?, ?, ?)"""
        args = [_count, _nationname, _capacity,  _suppkey, _nationkey]
        _conn.execute(sql, args)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    
def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    try:
        sql = """SELECT *
                FROM warehouse;"""
        cur = _conn.cursor()
        cur.execute(sql)
        

        l = f"{'w_warehousekey':>10} {'w_name':^30} {'w_capacity':^30} {'w_suppkey':^30} {'s_nationkey':^30}\n"
        with open("output/1.out", "w") as f:
            f.write(l)
        rows = cur.fetchall()
        for row in rows: 
            l = f"{row[0]:>14} {row[1]:<} {row[2]:>20} {row[3]:>30} {row[4]:>30}\n" 
            with open("output/1.out", "a") as f:
                f.write(l)
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    try:
        sql = """SELECT COUNT(DISTINCT w_warehousekey) as wkey_count, SUM(w_capacity) as tot_cap, n_name
               FROM nation, warehouse
               WHERE w_nationkey = n_nationkey
               GROUP BY n_name
               ORDER BY wkey_count DESC, n_name ASC"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        l = f"{'wkey_count':^10} {'tot_cap':^30} {'n_name':^30}\n"
        with open("output/2.out", "w") as f:
            f.write(l)
        rows = cur.fetchall()
        for row in rows: 
            l = f"{row[0]:^10} {row[1]:^30} {row[2]:^30}\n" 
            with open("output/2.out", "a") as f:
                f.write(l)
    except Error:
        _conn.rollback()
        print(Error)

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    try:
        input = open("input/3.in", "r")
        nation = input.readline().strip()
        input.close()

        sql = """SELECT s_name, n_name, w_name
                FROM supplier, nation, warehouse
                WHERE n_name = ?
                AND n_nationkey = s_nationkey
                AND s_nationkey = w_nationkey
                AND w_suppkey = s_suppkey
                GROUP BY s_name
                ORDER BY w_name ASC;"""
        cur = _conn.cursor()
        cur.execute(sql, (nation, ))


        l = f"{'supplier':<14} {'nation':^28} {'warehouse':>14}\n"
        with open("output/3.out", "w") as f:
            f.write(l)
        rows = cur.fetchall()
        for row in rows: 
            l = f"{row[0]:>14} {row[1]:^20} {row[2]:>20}\n"
            with open("output/3.out", "a") as f:
                f.write(l)
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    try:
        input = open("input/4.in", "r")
        region = input.readline().strip()
        cap = input.readline().strip()
        input.close()

        # print(region)
        # print(cap)

        sql = """SELECT w_name, w_capacity
                FROM warehouse, region
                WHERE w_capacity > ?
                AND r_name = ?
                AND w_nationkey IN (
                    SELECT n_nationkey 
                    FROM region r, nation n
                    WHERE r.r_name = ?
                    AND r.r_regionkey = n.n_regionkey)
                ORDER BY w_capacity DESC """
        cur = _conn.cursor()
        args = [cap, region, region]
        cur.execute(sql, args)

        l = f"{'w_name':^20} {'w_capacity':^30}\n"
        with open("output/4.out", "w") as f:
            f.write(l)
        rows = cur.fetchall()
        for row in rows: 
            l = f"{row[0]:^20} {row[1]:^20}\n" 
            with open("output/4.out", "a") as f:
                f.write(l)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    try:
        input = open("input/5.in", "r")
        nation = input.readline().strip()
        input.close()

        sql = """SELECT r_name, SUM(w_capacity)
            FROM nation, region, warehouse
                WHERE n_name = ? AND 
                    n_regionkey = r_regionkey AND 
                    n_nationkey = w_nationkey
                    GROUP BY r_regionkey"""
        cur = _conn.cursor()
        cur.execute(sql, (nation, ))


        l = f"{'region':^20} {'capacity':^30}\n"
        with open("output/5.out", "w") as f:
            f.write(l)
        rows = cur.fetchall()
        for row in rows: 
            l = f"{row[0]:^20} {row[1]:^20}\n" 
            with open("output/5.out", "a") as f:
                f.write(l)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
