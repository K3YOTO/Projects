#Connecting to the Database
import sqlite3
import pathlib
import os

#Random Invoice generator
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range (length))
    return result_str


def connectionpath(dp_path: str) -> sqlite3.Connection:
    path_to_db = pathlib.Path(dp_path).absolute().as_uri()
    print(path_to_db)
    connection = None
    try:
        connection = sqlite3.connect(f"{path_to_db}?mode=rw", uri=True)
    except:
        print(
              f"Error trying to open Database, please check path: {path_to_db}"
              )
        os.sys.exit(1)
    return connection

if __name__ == "__main__":
    local_db_path = "./Capstone.db"
    error_db_path = "DELETE_ME.db"
    #con = method_1(error_db_path)
    con = connectionpath(local_db_path)

    db_cur = con.cursor()

    #Customer/invoices info SQL command
    sqli = """INSERT INTO Invoices(Name,Contactnum, Email, Address, InvoiceNum, InvoiceDate)
            VALUES(?,?,?,?,?,?)"""
    #Product SQL Command to insert
    sqlp = """INSERT INTO products(sku, prodname, retailprice)
        VALUES(?,?,?)"""
    i = 0
    vals = []
    sqlran = """INSERT INTO """

    data = (142632, "Generic TV 55 Inch", 1499.99)

    db_cur.execute(sqlp, data)

    con.commit()
    con.close()