import sqlite3


# CONNECT = sqlite3.connect(":memory")
CONNECTION = sqlite3.connect('data_collection.db')

CURSOR_ = CONNECTION.cursor()

CURSOR_.execute("""CREATE TABLE data_collection(
                

)





""")

