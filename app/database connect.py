
import psycopg2
uri="postgres://wttxpbzwwyiezo:da62a0b0a27d53b8c813a6eb60df65b636c162a4df0336c00409558a5c3f2c14@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dimfu044kiidh"


#command="CREATE TABLE abhi_table(Temperature INTEGER, Distance FLOAT, Led1 BOOL, Led2 BOOL)"
#command="INSERT INTO abhi_table (Temperature, Distance, Led1, Led2) VALUES(35, 10.2, TRUE, FALSE)"
command="SELECT Led1, Led2 FROM abhi_table"
conn=psycopg2.connect(uri, sslmode='require')
cur=conn.cursor()
cur.execute(command)

led1,led2=cur.fetchone()
print(led1)
#conn.commit()

conn.close()
