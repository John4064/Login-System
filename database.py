
from config import *
import pyodbc



if __name__ == '__main__':
    try:
        cnxn = pyodbc.connect('DRIVER=' + driver +
                              ';SERVER=' + DATABASE_URL +
                              ';DATABASE=' + database +
                              ';UID=' + username +
                              ';PWD=' + dbpassword)

        cursor = cnxn.cursor()
        print('Connection established')
    except:
        print('Cannot connect to SQL server')

