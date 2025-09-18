from .connect import get_connect

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