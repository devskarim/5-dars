from database import query_sql 


query_sql ("""

CREATE TABLE universities (
    university_id SERIAL PRIMARY KEY,
    university_name VARCHAR(100) NOT NULL
);

CREATE TABLE faculties (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    university_id INT REFERENCES universities(university_id) ON DELETE CASCADE
);


""",commit=True)


query_sql ("""

INSERT INTO universities (university_name) VALUES
		('Tashkent State University'),
		('Samarkand State University');

INSERT INTO faculties (faculty_name, university_id) VALUES
		('Computer Science', 1),
		('Mathematics', 1),
		('Physics', 1),
		('History', 2),
		('Philology', 2);


""",commit=True)

data = query_sql ("""
	SELECT 
			u.university_name,
			f.faculty_name
	FROM universities u
	JOIN faculties f ON u.university_id = f.university_id
	ORDER BY u.university_name;



""",fetchall=True) 


print(data)