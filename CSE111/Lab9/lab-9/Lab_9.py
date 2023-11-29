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


def create_View1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")

    try: 
        sql = """CREATE VIEW V1(c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, c_nation,c_region) AS
                    SELECT c_custkey,
                    c_name, 
                    c_address, 
                    c_phone, 
                    c_acctbal, 
                    c_mktsegment, 
                    c_comment, 
                    n_name,
                    r_name 
                        FROM customer, nation, region
                        WHERE c_nationkey = n_nationkey AND 
                                    n_regionkey = r_regionkey"""

        _conn.execute(sql)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try: 
        sql = """SELECT V1.c_nation as country, COUNT(V1.c_custkey) as cnt FROM orders, V1
                    WHERE o_custkey = V1.c_custkey AND
                            V1.c_region = 'EUROPE'
                                GROUP BY V1.c_nation"""
        
        cur = _conn.cursor()
        cur.execute(sql)

    except Error as e:
        _conn.rollback()
        print(e)

    try:
        output = open('output/1.out', 'w')

        header = "{}|{}"
        output.write((header.format("country", "cnt")) + '\n')
        rows = cur.fetchall()
        for row in rows: 
            output.write((header.format(row[0], row[1])) + '\n')

        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")
    try: 
        sql = """CREATE VIEW V2(o_orderkey, o_custkey, o_orderstatus,
                            o_totalprice, o_orderyear, o_orderpriority,
                            o_clerk, o_shippriority, o_comment) AS
                        SELECT o_orderkey, 
                        o_custkey, 
                        o_orderstatus, 
                        o_totalprice, 
                        strftime('%Y',o_orderdate), 
                        o_orderpriority, 
                        o_clerk, 
                        o_shippriority, 
                        o_comment 
                        from orders;"""
        

        _conn.execute(sql)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")


    try:
        output = open('output/2.out', 'w')
        sql = """SELECT V1.c_name as customer, COUNT(*) as cnt
                    FROM V1, V2
                    WHERE V2.o_custkey = V1.c_custkey AND
                            V1.c_nation = 'EGYPT' AND 
                                V2.o_orderyear = '1992'
                                GROUP BY V1.c_name"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        header = "{}|{}"
        output.write((header.format("customer", "cnt")) + '\n')

        rows = cur.fetchall()

        for row in rows:
            output.write((header.format(row[0], row[1])) + '\n')

        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    try:
        output = open('output/3.out', 'w')

        sql = """SELECT V1.c_name as customer, sum(V2.o_totalprice) as total_price
                    FROM V1, V2
                    WHERE V2.o_custkey = V1.c_custkey AND 
                            V1.c_nation = 'ARGENTINA' AND 
                            V2.o_orderyear = '1996'
                            GROUP BY V1.c_name"""
        
        cur = _conn.cursor()
        cur.execute(sql)     

        header = "{}|{}"
        output.write((header.format("customer", "total_price")) + '\n')

        rows = cur.fetchall()

        for row in rows:
            output.write((header.format(row[0], row[1])) + '\n')

        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V4")

    try:
        sql= """CREATE VIEW V4(s_suppkey,
                s_name, 
                s_address, 
                s_phone, 
                s_acctbal, 
                s_comment, 
                s_nation, 
                s_region) AS
            SELECT s_suppkey, s_name, s_address, s_phone,
                    s_acctbal, s_comment, n_name, r_name
            FROM supplier, nation, region
            WHERE s_nationkey = n_nationkey AND 
                    n_regionkey = r_regionkey"""
        
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    try:

        sql = """SELECT V4.s_name as supplier, COUNT(*) as cnt
                FROM partsupp, V4, part
                WHERE ps_suppkey = V4.s_suppkey AND 
                        V4.s_nation = 'KENYA' AND 
                            ps_partkey = p_partkey AND 
                                p_container LIKE '%BOX%'
                                GROUP BY V4.s_name"""
        
        cur = _conn.cursor()
        cur.execute(sql)  

        output = open('output/4.out', 'w')

        header = "{}|{}"
        output.write((header.format("supplier", "cnt")) + '\n')

        rows = cur.fetchall()
        for row in rows: 
            output.write((header.format(row[0], row[1])) + '\n')            

        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")


    try:
        sql="""SELECT V4.s_nation as country, COUNT(*) as cnt
                FROM V4
                WHERE (V4.s_nation = 'ARGENTINA' OR
                        V4.s_nation = 'BRAZIL')
                        GROUP BY V4.s_nation"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/5.out', 'w')

        header = "{}|{}"
        output.write((header.format("country", "cnt")) + '\n')

        rows = cur.fetchall()

        for row in rows:
            output.write((header.format(row[0], row[1])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    try:
        sql = """SELECT V4.s_name as supplier,
                        o_orderpriority as priority,
                            COUNT(DISTINCT ps_partkey) as parts
                FROM partsupp, orders, lineitem, V4
                WHERE l_orderkey = o_orderkey AND 
                        l_partkey = ps_partkey AND 
                            l_suppkey = ps_suppkey AND
                                ps_suppkey = V4.s_suppkey AND 
                                    V4.s_nation = 'INDONESIA'
                        GROUP BY V4.s_name, o_orderpriority"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/6.out', 'w')

        header = "{}|{}|{}"
        output.write((header.format("supplier", "priority", "parts")) + '\n')

        rows = cur.fetchall()

        for row in rows:
            output.write((header.format(row[0], row[1], row[2])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    try:
        sql = """SELECT V1.c_nation as country, 
                        V2.o_orderstatus as status,
                            COUNT(*) as orders
                FROM V2, V1
                WHERE V2.o_custkey = V1.c_custkey AND 
                        V1.c_region = 'AFRICA'
                        GROUP BY V1.c_nation, V2.o_orderstatus"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/7.out', 'w')

        header = "{}|{}|{}"
        output.write((header.format("country", "status", "orders")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1], row[2])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")

    try:
        sql = """SELECT COUNT(DISTINCT V2.o_clerk) as clerks
                FROM V2, lineitem, V4
                WHERE V2.o_orderkey = l_orderkey AND 
                        l_suppkey = V4.s_suppkey AND 
                        V4.s_nation = 'PERU'"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/8.out', 'w')

        header = "{}"
        output.write((header.format("clerks")) + '\n')

        rows = cur.fetchall()

        for row in rows:
            output.write((header.format(row[0])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    try:
        sql = """SELECT V4.s_nation as country, COUNT(DISTINCT l_orderkey) as cnt
                    FROM lineitem, V2, V4
                    WHERE l_orderkey = V2.o_orderkey AND 
                            l_suppkey = V4.s_suppkey AND
                            V2.o_orderstatus = 'F' AND 
                                V2.o_orderyear = '1993' AND 
                                V4.s_region = 'AFRICA'
                                GROUP BY V4.s_nation
                                HAVING cnt > 200"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/9.out', 'w')

        header = "{}|{}"
        output.write((header.format("country", "cnt")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")
    try:
        sql= """CREATE VIEW V10(p_type, min_discount, max_discount) AS
                SELECT p_type, MIN(l_discount), MAX(l_discount)
                FROM lineitem, part
                WHERE l_partkey = p_partkey
                GROUP BY p_type"""
        
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    try:

        sql = """SELECT V10.p_type as part_type,
                    V10.min_discount as min_disc,
                    V10.max_discount as max_disc
            FROM V10 
            WHERE (V10.p_type like '%ECONOMY%'
                or V10.p_type like '%COPPER%')
            group by V10.p_type"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        
        
        output = open('output/10.out', 'w')

        header = "{}|{}|{}"
        output.write((header.format("part_type", "min_disc", "max_disc")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1], row[2])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View111(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V111")

    try:
        sql= """CREATE VIEW V111(c_custkey, c_name, c_nationkey, c_acctbal) AS
                SELECT c_custkey, c_name, c_nationkey, c_acctbal
                FROM customer
                WHERE c_acctbal < 0"""
        
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")


def create_View112(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V112")

    try:
        sql= """CREATE VIEW V112(s_suppkey, s_name, s_nationkey, s_acctbal) AS
                SELECT s_suppkey, s_name, s_nationkey, s_acctbal
                FROM supplier
                WHERE s_acctbal > 0"""
        
        _conn.execute(sql)
        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")


    try:
        sql = """SELECT COUNT(DISTINCT l_orderkey) as order_cnt
                FROM lineitem, V112, orders, V111
                WHERE l_orderkey = o_orderkey AND 
                        o_custkey = V111.c_custkey AND 
                            l_suppkey = V112.s_suppkey"""
        output = open('output/11.out', 'w')

        cur = _conn.cursor()
        cur.execute(sql)

        header = "{}"
        output.write((header.format("order_cnt")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")


    try:
        sql = """SELECT V4.s_region as region, MAX(V4.s_acctbal) as  max_bal
            FROM V4
            GROUP BY V4.s_region
            HAVING max_bal > 9000"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/12.out', 'w')

        header = "{}|{}"
        output.write((header.format("region", "max_bal")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    try:
        sql = """SELECT V4.s_region as supp_region,
                    V1.c_region as cust_region, 
                    MIN(o_totalprice) as min_price
            FROM lineitem, V4, V1, orders
            WHERE l_orderkey = o_orderkey AND 
                    o_custkey = V1.c_custkey AND 
                    l_suppkey = V4.s_suppkey
                    GROUP BY V4.s_region, V1.c_region"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        
        output = open('output/13.out', 'w')

        header = "{}|{}|{}"
        output.write((header.format("supp_region", "cust_region", "min_price")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1], row[2])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    try:
        sql="""SELECT COUNT(*) as items
                FROM lineitem, V1, V2, V4
                WHERE l_orderkey = V2.o_orderkey AND 
                        V2.o_custkey = V1.c_custkey AND 
                        V1.c_nation = 'KENYA' AND 
                        l_suppkey = V4.s_suppkey AND 
                        V4.s_region = 'ASIA' """
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/14.out', 'w')

        header = "{}"
        output.write((header.format("items")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0])) + '\n')


        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    try:
        sql = """SELECT V4.s_region, V4.s_name, V4.s_acctbal
                FROM V4 
                GROUP BY V4.s_region 
                HAVING V4.s_acctbal = MAX(V4.s_acctbal)
                ORDER BY V4.s_name ASC"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        output = open('output/15.out', 'w')

        header = "{}|{}|{}"
        output.write((header.format("region", "supplier", "acct_bal")) + '\n')

        rows = cur.fetchall()

        for row in rows: 
            output.write((header.format(row[0], row[1], row[2])) + '\n')

        output.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)

        create_View4(conn)
        Q4(conn)

        Q5(conn)
        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        create_View111(conn)
        create_View112(conn)
        Q11(conn)

        Q12(conn)
        Q13(conn)
        Q14(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
