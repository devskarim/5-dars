from psycopg2 import connect
from environs import Env



mydb = connect(
    user="postgres",
    password="hcnma_$",
    host="localhost",
    port=5432,
    database="fn33_homework",
)

print("succces")
