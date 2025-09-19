from database import query_sql

query_sql(
    """
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_title VARCHAR(100) NOT NULL
);

CREATE TABLE author_books (
    author_id INT REFERENCES authors(author_id) ON DELETE CASCADE,
    book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
    PRIMARY KEY (author_id, book_id)
);
""",
    commit=True,
)


query_sql(
    """
INSERT INTO authors (author_name) VALUES
    ('J.K. Rowling'),
    ('Stephen King'),
    ('George R.R. Martin');

INSERT INTO books (book_title) VALUES
    ('Harry Potter'),
    ('The Shining'),
    ('Game of Thrones'),
    ('Fantasy Collaboration');

INSERT INTO author_books (author_id, book_id) VALUES
    (1, 1),  -- Rowling -> Harry Potter
    (2, 2),  -- King -> The Shining
    (3, 3),  -- Martin -> Game of Thrones
    (1, 4),  -- Rowling -> Fantasy Collaboration
    (3, 4);  -- Martin -> Fantasy Collaboration
""",
    commit=True,
)


data = query_sql(
    """
SELECT 
    b.book_title,
    STRING_AGG(a.author_name, ', ') AS authors
FROM books b
JOIN author_books ab ON b.book_id = ab.book_id
JOIN authors a ON ab.author_id = a.author_id
GROUP BY b.book_id, b.book_title
ORDER BY b.book_title;
""",
    fetchall=True,
)

print(data)
