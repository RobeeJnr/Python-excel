import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='4444.44robee',
    db='downloads')
cursor = mydb.cursor()

csv_data = csv.reader('the-outpost.csv')
for row in csv_data:

    cursor.execute('INSERT INTO series(episode_name, episode_link ) VALUES("%s", "%s")',row)
#close the connection to the database.
    mydb.commit()
    cursor.close()
    print ("Done")
