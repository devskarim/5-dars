from database import query_sql


query_sql("""
			CREATE TABLE IF NOT EXISTS users(
						id SERIAL PRIMARY KEY, 
						name VARCHAR(50) NOT NULL, 
						lastname VARCHAR(50) NOT NULL
								 )
""", commit=True)

query_sql("""
			CREATE TABLE IF NOT EXISTS passports(
					id SERIAL PRIMARY KEY, 
					user_id INT REFERENCES users(id), 
					passport_number VARCHAR(50) NOT NULL
					)

""",commit=True)


query_sql("""
		INSERT INTO users(name, lastname) VALUES ('Ali', 'Valiyev'), ('Vali', 'Aliyev') 
""", commit=True) 


query_sql("""
	INSERT INTO passports(user_id, passport_number) VALUES (1, 'AD12345'),( 2, 'AE12321') 

""")

data = query_sql("""
SELECT u.name as  user_name, passports.passport_number from users   JOIN passports on user.id = passports.user_id

""", fetchall= True) 

print(data)
