from psycopg2 import connect 

mydb = connect(
	username = "postgres", 
	password = "hcnma_$", 
	host = "localhost", 
	port = 5432, 
	database = "fn33_homework" 
)


print("succces") 