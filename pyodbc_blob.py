import pyodbc # pip install pyodbc
import os

def con_win_authen():
    driver = 'ODBC Driver 13 for SQL Server'
    server = '.'
    database = 'demo2016'
    return f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

def con_sql_authen():
    driver = 'ODBC Driver 13 for SQL Server'
    server = 'p1.acc.chula.ac.th'
    database = 'demo2016'
    uid = 'user'
    pwd = 'password'
    return f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'

def create_table():
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            CREATE TABLE media(
              id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
              descr VARCHAR(255),
              filetype VARCHAR(30),
              stream VARBINARY(MAX)
            )
        """
        con.execute(sql_cmd)


def read_bin(filename):
    with open(filename, mode='rb') as f:
        return f.read()


def write_bin(filename, data):
    with open(filename, mode='wb') as f:
        f.write(data)


def insert_data(params):
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
           INSERT INTO media(descr, filetype, stream) VALUES(?, ?, ?)
        """
        con.execute(sql_cmd, params)


def select_data(params, outfile=None):
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            SELECT stream, descr, filetype FROM media WHERE id = ?;
         """
        for row in con.execute(sql_cmd, params):
            if not (outfile):
                outfile = f'{row[1]}.{row[2]}'
            write_bin(outfile, row[0])


def filename_ext(fullpath):
    # fullpath = r'Z:\prasert\Dropbox\PycharmProjects\mssql_mysql_tutor\product\mic.png'
    basename = os.path.basename(fullpath)  # return filename.ext (no path)
    filename, ext = os.path.splitext(basename)
    # print(f'filename = # filename}, ext = {ext}')
    return filename, ext[1:]


def insert_files_in_folder(folder, ext_filter):
    for basename in os.listdir(folder):
        if basename.endswith('.' + ext_filter):
            filename, ext = os.path.splitext(basename)
            # print(filename, ext[1:])
            # print(folder, basename)
            print(os.path.join(folder, basename))
            insert_data((filename, ext[1:], read_bin(os.path.join(folder, basename))))


if __name__ == '__main__':
    con_string = con_win_authen()
    # create_table()
    # insert_data(('Archery', 'png', read_bin(r'images/Archery.png')))
    # insert_data(('sample spreadsheet', 'xlsx', read_bin(r'images/sample.xlsx')))
    # insert_data(('big tablet', 'png', read_bin(r'images/tablet.png')))
    # insert_data(('simple text file', 'txt', read_bin(r'images/demo.txt')))
    # select_data(2)
    # select_data(2, 'demo.xlsx')
    # select_data(2, 'test1.png')
    # select_data(3, 'test.txt')
    # insert_files_in_folder(r'images', 'png')
    # select_data(3)