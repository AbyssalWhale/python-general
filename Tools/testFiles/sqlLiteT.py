import sqlite3
import json
from pathlib import Path


# Write
MOVIES_DATA = json.loads(Path("Tools/testFiles/movies.json").read_text())

with sqlite3.connect("db.sqlite3") as connectionString:
    sqlCommand = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in MOVIES_DATA:
        connectionString.execute(sqlCommand, tuple(movie.values()))
    connectionString.commit()

# Read
with sqlite3.connect("db.sqlite3") as connectionString:
    sqlCommand = "SELECT * FROM Movies"
    cursor = connectionString.execute(sqlCommand)
    for row in cursor:
        print(row)
    # to get all rows
    movies = cursor.fetchall()
    print(movies)
