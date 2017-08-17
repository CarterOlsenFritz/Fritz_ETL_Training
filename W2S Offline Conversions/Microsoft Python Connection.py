"""
This is Microsoft's example of using python to query an Azure db.
https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python

Windows: Install the newest version of Python (environment variable is now configured for you), install the ODBC driver and SQLCMD, and then install the Python Driver for SQL Server. See Step 1.2, 1.3, and 2.1.

#How to set up pymssql for Python
https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development

"""

#import os #Not necessary right now?

from credentials_sql import * # Grabbing the credentials from different python file. I am removing the credentials_sql.py from github for security purposes.
import pyodbc
import datetime

driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM [dbo].[ES_Wheretostay_Offline_Conversions] order by [e_id]")
row = cursor.fetchone()
#row = cursor.fetchall()
#row = cursor.fetchmany(10)
while row:
    #print (str(row[0]) + " " + str(row[1]))
    print(row)
    row = cursor.fetchone() # This line iterates down one row and then stops the above query from running forever? When I remove it, this section prints the first row forever.
