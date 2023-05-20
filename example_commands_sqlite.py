import sqlite3

# Connect to the database
conn = sqlite3.connect('reviews.db')

# Create a cursor object
c = conn.cursor()

# Select all columns from the movie_reviews table
c.execute("SELECT * FROM movie_reviews")

# Fetch allrows from the query result as a list of tuples
movie_reviews = c.fetchall()

# Print the movie reviews
print("Movie Reviews:")
for review in movie_reviews:
    print(review)

# Select all columns from the finantials table
c.execute("SELECT * FROM finantials")

# Fetch all rows from the query result as a list of tuples
finantials = c.fetchall()

# Print the finantials data
print("\nFinantials:")
for data in finantials:
    print(data)

# Join the movie_reviews and finantials tables on the title column
c.execute('''
    SELECT movie_reviews.title, movie_reviews.rating, finantials.earnings, finantials.budget
    FROM movie_reviews 
    JOIN finantials ON movie_reviews.title = finantials.title
''')

# Fetch all rows from the query result as a list of tuples
movie_data = c.fetchall()

# Print the joined data
print("\nMovie Data:")
for data in movie_data:
    print(data)

# Insert a new row into the movie_reviews table
c.execute("INSERT INTO movie_reviews VALUES ('2022-05-20', 'The Matrix', 8)")

# Commit changes to the database
conn.commit()

# Select all columns from the movie_reviews table
c.execute("SELECT * FROM movie_reviews")

# Fetch all rows from the query result as a list of tuples
movie_reviews = c.fetchall()

# Print the updated moviereviews
print("\nUpdated Movie Reviews:")
for review in movie_reviews:
    print(review)

# Close the database connection
conn.close()