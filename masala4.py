from database import query_sql


query_sql(
    """

CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE
);


""",
    commit=True,
)


query_sql(          
    """
    INSERT INTO teachers (teacher_name) VALUES
        ('Mr. Smith'),
        ('Ms. Johnson');

    INSERT INTO students (student_name, teacher_id) VALUES
        ('Ali', 1),
        ('Vali', 1),
        ('Karim', 1),
        ('Laylo', 2),
        ('Malika', 2);


""",commit=True
)


data =  query_sql(
    """
    SELECT 
        t.teacher_name,
        s.student_name
    FROM teachers t
    JOIN students s ON t.teacher_id = s.teacher_id
    ORDER BY t.teacher_name;


""", fetchall=True 
)


print(data)