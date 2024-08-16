import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='102318@#11',database='testdb')
stmt=con.cursor()
query='select * from emp;'
stmt.execute(query)
data=stmt.fetchone()
print(data)


