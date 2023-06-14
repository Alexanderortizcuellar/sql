import duckdb

con = duckdb.connect("duck.db")
cursor = con.cursor()
#  cursor.execute("CREATE TABLE customers2(customer TEXT,age INT,city TEXT)")
#cursor.execute("INSERT INTO customers2 VALUES('alex',22,'bogota'),('emily',21,'mosquera'),('nelly',59,'briceño')")
cursor.execute("select * from information_schema.columns where table_name='customers'")
print(cursor.fetchall())

con.close()


