from database import query_sql 

query_sql("""
CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(50) NOT NULL
);

CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE
);


""",commit=True)


query_sql("""
INSERT INTO teachers (teacher_name) VALUES
	('Mr. Brown'),
	('Ms. White');

INSERT INTO subjects (subject_name, teacher_id) VALUES
	('Mathematics', 1),
	('Physics', 1),	
	('Chemistry', 1),
	('English', 2),
	('History', 2);


""",commit=True)


data = query_sql("""
	SELECT 
			t.teacher_name,
			s.subject_name
	FROM teachers t
	JOIN subjects s ON t.teacher_id = s.teacher_id
	ORDER BY t.teacher_name;


""",fetchall=True)

print(data)