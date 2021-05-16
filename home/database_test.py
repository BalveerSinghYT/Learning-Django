import psycopg2

def markAttendance(name):
	with open('attendance.csv', 'r+') as f:         # r+ mean read & write
		myDataList = f.readlines()
		nameList = []
		for line in myDataList:
			entry = line.split(',')
			nameList.append(entry[0])
		if name not in nameList:
			now = datetime.now()
			dtstring = now.strftime('%H:%M:%S')
			f.writelines(f'\n{name}, {dtstring}')

name = 'Elon Musk'

#establishing the connection
conn = psycopg2.connect(
   database="AttendanceDB", user='postgres', password='veer', host='127.0.0.1', port= '5432'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''SELECT roll_no FROM public.home_registeration where name = '%s';'''%name)

#Fetching 1st row from the table
result = cursor.fetchall()

cursor.execute('''INSERT INTO home_attendance(date, status, roll_no_id)
	VALUES ('2021-06-17', 'present', %s)''', result[0])  

# Commit your changes in the database
conn.commit()

print("Records inserted........")

# Closing the connection
conn.close()