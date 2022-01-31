import mysql.connector

mydb = mysql.connector.connect(
    host = "67.80.182.230",
    user = "john4064",
    password = "Panda1234"

)


if __name__ == '__main__':
    print(mydb)