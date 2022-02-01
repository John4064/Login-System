import mysql.connector

"""
mydb = mysql.connector.connect(
    host = "67.80.182.230",
    user = "john4064",
    password = "Panda1234"

)
"""
import random

def init(n : int)-> list[int]:
    ansArr=[]

    return ansArr

if __name__ == "__main__":
    generators = init(5)

    if generators is not None:
        for rnd in generators:
            print(rnd.randint(0, 1000))

