'''
write a python Script to list out all document of Employee_Colle which is the collection 
of Practice_DB Where esal is greater then 2000 and less than 5000
'''
print(f'Question: {__doc__}')

from pymongo import MongoClient
con = MongoClient('localhost',port=27017)
db = con['Practice_DB']
coll = db['Employee_Coll']
documents = coll.find({'$and':[{'esal':{'$gt':2000}},{'esal':{'$lt':5000}}]})
for doc in documents:
	print(doc)
	print('-'*80)
con.close()

print('#'*95)

from pymysql import connect
con = connect(host='localhost',user='root',port=3306, password='1234',database='employee')
cursor = con.cursor()
cursor.execute('select * from employee_table where esal > 20000 and esal<50000')
all_data = cursor.fetchall()
for data in all_data:
	print(f'id: {data[0]} | Employee No: {data[1]} | Employee Name: {data[2]} | Employee Address: {data[3]} | Employee Salary: {data[4]}')