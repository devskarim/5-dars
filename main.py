from psycopg2 import connect 
from environs import Env 

env = Env() 
env.read_env() 

def get_connect(): 

	return  connect( 
		user = env.str("DB_USER"),
		password = env.str("DB_PASSWORD"),
		dbname = env.str("DB_DATABASE"),
		host = env.str("DB_HOST"),
		port = env.str("DB_PORT")
)

def query_sql(query,*args , fetchone=False, fetchall=False, commit=False):
	try:
		with get_connect() as db:
			db.autocommit = True
			with db.cursor() as dbc: 
				dbc.execute(query,args or ())
				if fetchone:
					return dbc.fetchone() 
				if fetchall: 
					return dbc.fetchall() 
			if commit:
				return True 
	except:
		return None 