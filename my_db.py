import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by db_file
    :param db_file:
    :return:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


def execute_sql(conn_sql):
    """ Execute sql
        :param conn: Connection object
        :param sql: a SQL script
        :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)
        

if __name__ == '__main__':
    create_machine_sql = """
    --machine table
    CREATE TABLE IF NOT EXIST rsk_mach (
    id integer PRIMARY KEY
    ,machine_id integer NOT_NULL
    ,machine_name text
    ,kind text NOT NULL
    ,operation_number integer NOT NULL
    ,medium_electricity boolean NOT NULL
    ,medium_electricity_consumption decimal(10,4)
    ,medium_gas boolean NOT NULL
    ,medium_gas_consumption decimal(10,4)
    ,medium_air boolean NOT NULL
    ,medium_air_consumption decimal(10,4)
    ,medium_water boolean NOT NULL
    ,medium_water_consumption decimal(10,4)
    )
    """
    create_casting_machine_sql = """
    --machine for casting
    CREATE TABLE IF NOT EXIST rsk_cast_mach (
    id integer PRIMARY KEY
    ,casting_machine_id integer NOT NULL
    ,casting_machine_name text
    ,casting_method_gravity boolean NOT NULL
    ,cooling_air_qty integer
    ,cooling_water_qty integer
    ,casting_furnace_vol integer
    )
    """
    db_file = 'kokile_machines.db'
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_machine_sql)
        execute_sql(conn, create_casting_machine_sql)
        conn.close()
        
        
def add_machine(conn, machine):
    """
    Create new machine into machine table
    :param conn:
    :param machine:
    :return:
    """
    sql = '''
    INSERT INTO machines( machine_id,machine_name,kind text,operation_numberL
    ,medium_electricity,medium_electricity_consumption
    ,medium_gas,medium_gas_consumption
    ,medium_air,medium_air_consumption
    ,medium_water,medium_water_consumption
    VALUES(?,?,?,?,?,?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, machine)
    conn.commit()
    return cur.lastrowid


def select_machines_by_kind(conn, kind):
    """
    Query kiind by kind
    :param conn:
    :param kind:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM machines WHERE kind=?", (kind,))
    rows = cur.fetchall()
    return rows


def select_all(conn, table):
    """
    Query all rows in the table
    :param conn:
    :param table:
    :return:
    """
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows


def select_where_parametr(conn, table, **query):
    """
    Query tasks from table with data from **query dict
    :param conn:
    :param table:
    :param query:
    :return:
    """
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f'{k}=?')
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f'SELECT * FROM {table} WHERE {q}', values)
    rows = cur.fetchall()
    return rows


def update(conn, table, id, **kwargs):
    """
    update all parameters of a machine
    :param conn:
    :param table:
    :param id:
    :param kwargs:
    :return:
    """
    parameters = [f'{k} = ?' for k in kwargs]
    parameters = ', '.join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )
    sql = f'''
    UPDATE {table}
    SET {parameters}
    WHERE id = ?
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)