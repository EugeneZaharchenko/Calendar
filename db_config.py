from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'eugene'
app.config['MYSQL_DATABASE_PASSWORD'] = '1401'
app.config['MYSQL_DATABASE_DB'] = 'FlaskCalendar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
