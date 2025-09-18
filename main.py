from psycopg2 import connect 
from environs import Env 

env = Env() 
env.read_env() 

mydb = connect(
	user = env.str("DB_USER"),
	password = env.str("DB_PASSWORD"),
	dbname = env.str("DB_NAME"),
	host = env.str("DB_HOST"),
	port = env.str("DB_PORT")

)



print("DATABASE connected succesfully")  