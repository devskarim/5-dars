from database import query_sql 


query_sql("""
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name VARCHAR(100) NOT NULL
);

CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_title VARCHAR(100) NOT NULL
);

CREATE TABLE actor_movies (
    id SERIAL PRIMARY KEY,
    actor_id INT REFERENCES actors(actor_id) ON DELETE CASCADE,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE
);


""",commit=True)

query_sql("""
INSERT INTO actors (actor_name) VALUES
	('Tom Hanks'),
	('Leonardo DiCaprio'),
	('Brad Pitt');

INSERT INTO movies (movie_title) VALUES
	('Inception'),
	('Fight Club'),
	('Forrest Gump');

INSERT INTO actor_movies (actor_id, movie_id) VALUES
	(1, 3),  -- Tom Hanks -> Forrest Gump
	(2, 1),  -- Leonardo -> Inception
	(3, 2),  -- Brad Pitt -> Fight Club
	(3, 1);  -- Brad Pitt -> Inception  


""", commit=True)

data = query_sql("""
	SELECT 
			m.movie_title,
			a.actor_name
	FROM movies m
	JOIN actor_movies am ON m.movie_id = am.movie_id
	JOIN actors a ON am.actor_id = a.actor_id
	ORDER BY m.movie_title;


""",fetchall=True)


print(data)
 