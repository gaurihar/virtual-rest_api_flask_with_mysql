from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
#MySQL configurations

app.config['MYSQL_DATABASE_USER'] =  "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "1210"
app.config['MYSQL_DATABASE_DB'] = "UserInfo"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql.init_app(app)
