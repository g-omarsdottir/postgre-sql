import psycopg2

# Variable to connect to database
connection = psycopg2.connect(database="chinook")
# print("Database connection successful")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only by "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query 5 - select only the albums with "artist_id" #51 on the "album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# Query 7
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["AC/DC"])

# Query 8
#cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["AC/DC"])

# Query 9
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["test"])

# Query 10 
# cursor.execute('SELECT * FROM "artist_id"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()


# close the connection
connection.close()

# for each individual result in the results, print results
for result in results:
    print(result)

