
import pymysql
from pymysql.cursors import DictCursor


def conn(*, host, port, database, user, passwd, charset='utf8'):
    conn = pymysql.connect(host=host, port=port, database=database,
                           user=user, passwd=passwd, charset=charset)
    return conn


def query(sql, *args, conn):
    with conn.cursor(cursor=DictCursor) as cursor:
        rows = cursor.execute(sql, args)
        results = cursor.fetchall()
        return results


def pagination(sql, *args, page, rows, conn):
    with conn.cursor(cursor=DictCursor) as cursor:
        _args = (*args, (page-1)*rows, rows)
        cursor.execute(sql+' limit %s, %s', _args)
        results = cursor.fetchall()
        return results


def execute(sql, *args, conn):
    with conn.cursor() as cursor:
        result = cursor.execute(sql, args)
        conn.commit()
        if result >= 1:
            return True
        else:
            return False


def showall_dept(conn):
    for data in query('select dno as no, dname as name, dloc as loc from tb_dept', conn=conn):
        print(data)


def showpage_dept(conn, page, rows):
    print('page', page,':')
    for data in pagination('select dno as no, dname as name, dloc as loc from tb_dept', page=page, rows=rows, conn=conn):
        print(data)
    print()


if __name__ == '__main__':
    database = {
        'host': 'www.ebankp.com',
        'port': 3306,
        'database': 'atest',
        'user': 'atest',
        'passwd': 'atest',
        'charset': 'utf8'
    }
    conn = conn(**database)

    showall_dept(conn)
    print(execute('insert into tb_dept values (%s, %s, %s)',
                  70, '开发部', '深圳', conn=conn))
    showall_dept(conn)
    showpage_dept(conn, 1, 4)
    showpage_dept(conn, 2, 4)
    showpage_dept(conn, 3, 4)

    print(execute('update tb_dept set dname=%s, dloc=%s where dno=%s',
                  'dev', 'shenzhen', 70, conn=conn))
    showall_dept(conn)
    print(execute('delete from tb_dept where dno=%s', 70, conn=conn))
    showall_dept(conn)
