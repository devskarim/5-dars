from database import query_sql 


query_sql("""
		CREATE TABLE IF NOT EXISTS countries(
					id SERIAL PRIMARY KEY, 
					name VARCHAR(50) not null
					)
 
""", commit=True) 


query_sql("""
		CREATE TABLE IF NOT EXISTS capitals(
							id SERIAL PRIMARY KEY, 
							name VARCHAR(50) not null unique, 
							country_id INT REFERENCES countries(id)
							)
""", commit=True) 


query_sql("INSERT INTO countries(name) VALUES ('uzbekistan'), ('Saudi')",commit=True) 




query_sql("INSERT INTO capitals(name, country_id) VALUES ('Tashkent', 1), ('Riyadh', 2)",commit=True) 


data = query_sql("""SELECT c.name AS country_name, cp.name AS capital_name
											FROM countries c
											JOIN capitals cp ON c.id = cp.country_id""",fetchall=True)

for i in data: 
	print(i) 