import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator 1", "year": 1989},
    {"id": 1, "title": "Terminator 2", "year": 1991}
]

# Convert from obj to string and write into file
STRING_AS_JSON = json.dumps(movies)
Path("Tools/testFiles/movies.json").write_text(STRING_AS_JSON)

FILE_DATA = Path("Tools/testFiles/movies.json").read_text()
movies = json.loads(FILE_DATA)
print(movies[0]["title"])
