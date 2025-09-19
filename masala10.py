from database import query_sql

query_sql(
    """
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(50) NOT NULL
);

CREATE TABLE employee_projects (
    employee_id INT REFERENCES employees(employee_id) ON DELETE CASCADE,
    project_id INT REFERENCES projects(project_id) ON DELETE CASCADE,
    PRIMARY KEY (employee_id, project_id)
);
""",
    commit=True,
)


query_sql(
    """
INSERT INTO employees (employee_name) VALUES
    ('Alice'),
    ('Bob'),
    ('Charlie');

INSERT INTO projects (project_name) VALUES
    ('AI System'),
    ('Website Redesign'),
    ('Mobile App');

INSERT INTO employee_projects (employee_id, project_id) VALUES
    (1, 1),  -- Alice -> AI System
    (1, 2),  -- Alice -> Website Redesign
    (2, 2),  -- Bob -> Website Redesign
    (3, 1),  -- Charlie -> AI System
    (3, 3);  -- Charlie -> Mobile App
""",
    commit=True,
)


data = query_sql(
    """
SELECT 
    e.employee_name,
    STRING_AGG(p.project_name, ', ') AS projects
FROM employees e
JOIN employee_projects ep ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id
GROUP BY e.employee_id, e.employee_name
ORDER BY e.employee_name;
""",
    fetchall=True,
)

print(data)
