# This allows me to connect to our Azure SQL database

"""
# Not sure what this portion does. Maybe allows access to the Azure Remote Server?
import base64


username = 'user'
password = 'pass'
base64string = base64.b64encode('%s:%s' % (username, password))
headers={'Authorization':'Basic %s' % base64string,'Content-Type':'application/json'}
"""

#database credentials # lowercase are for Microsoft Python Connection file, upper case are how Rudder did it.
server = HOST ="host"
USER="user"
password = PASSWORD="pass"
database = DATABASE="db"
username = 'user'
