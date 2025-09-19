from database import query_sql


query_sql(
    """
			CREATE TABLE users (
				user_id SERIAL PRIMARY KEY,
				name VARCHAR(50) NOT NULL)

""",
    commit=True,
)


query_sql(
    """
		CREATE TABLE products (
				product_id SERIAL PRIMARY KEY,
				product_name VARCHAR(100) NOT NULL,
				price NUMERIC(10,2) NOT NULL
)

""",
    commit=True,
)


query_sql(
    """
			CREATE TABLE orders (
				order_id SERIAL PRIMARY KEY,
				user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
				product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
				quantity INT NOT NULL
)

""",
    commit=True,
)


query_sql(
    """
INSERT INTO users (name) VALUES
		('Ali'), ('Vali'), ('Karim');""",
    commit=True,
)


query_sql(
    """

INSERT INTO products (product_name, price) VALUES
	('Laptop', 800.00),
	('Phone', 500.00),
	('Mouse', 20.00);


""",
    commit=True,
)


query_sql(
    """
		INSERT INTO orders (user_id, product_id, quantity) VALUES
				(1, 1, 2),   
				(2, 3, 5),  
				(3, 2, 1)
""",
    commit=True,
)


data = query_sql(
    """

			SELECT 
				u.name AS user_name,
				p.product_name,
				p.price AS product_price,
				o.quantity
		FROM orders o
		JOIN users u ON o.user_id = u.user_id
		JOIN products p ON o.product_id = p.product_id;


""", fetchall=True,
)

print(data)
