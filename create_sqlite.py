import sqlite3

# Connect to the database
conn = sqlite3.connect('reviews.db')

# Create a cursor object
c = conn.cursor()

# Create the movie_reviews table
c.execute('''
    CREATE TABLE movie_reviews (
        date TEXT,
        title TEXT,
        rating INTEGER
    )
''')

# Create the finantials table
c.execute('''
    CREATE TABLE finantials (
        title TEXT,
        earnings REAL,
        budget REAL
    )
''')

# Insert some sample data into the movie_reviews table
c.execute("INSERT INTO movie_reviews VALUES ('2022-01-01', 'The Godfather', 9)")
c.execute("INSERT INTO movie_reviews VALUES ('2022-01-02', 'The Shawshank Redemption', 10)")
c.execute("INSERT INTO movie_reviews VALUES ('2022-01-03', 'The Dark Knight', 8)")
c.execute("INSERT INTO movie_reviews VALUES ('2022-01-04', 'The Godfather: Part II', 9)")
c.execute("INSERT INTO movie_reviews VALUES ('2022-01-05', '12 Angry Men', 9)")

# Insert some sample data into the finantials table
c.execute("INSERT INTO finantials VALUES ('The Godfather', 245.1, 6.0)")
c.execute("INSERT INTO finantials VALUES ('The Shawshank Redemption', 58.3, 25.0)")
c.execute("INSERT INTO finantials VALUES ('The Dark Knight', 1.005, 185.0)")
c.execute("INSERT INTO finantials VALUES ('The Godfather: Part II', 193.0, 13.0)")
c.execute("INSERT INTO finantials VALUES ('12 Angry Men', 2.0, 0.35)")

# Commit changes to the database
conn.commit()

# Close the database connection
conn.close()