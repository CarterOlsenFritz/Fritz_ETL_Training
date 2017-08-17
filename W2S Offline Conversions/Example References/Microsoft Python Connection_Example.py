"""
This is Microsoft's example of using python to query an Azure db.
https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python

Windows: Install the newest version of Python (environment variable is now configured for you), install the ODBC driver and SQLCMD, and then install the Python Driver for SQL Server. See Step 1.2, 1.3, and 2.1.

"""


import pyodbc
server = 'your_server.database.windows.net'
database = 'your_database'
username = 'your_username'
password = 'your_password'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT 'PROD' as 'PROD' ,*   FROM [dbo].[ES_W2S_Offline_Conversions] order by [e_id]")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()