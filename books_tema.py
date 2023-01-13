from itertools import combinations_with_replacement
from turtle import title
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Utilizând cadrul SQLAlchemy şi baza de date SQLite, 
# creaţi tabelul Books care va conţine următoarele coloane:

# id – cheia primară;
# title – textul;
# year – int.

# CREATING TABLE
engine = create_engine('sqlite:///books.db', echo = True)
meta = MetaData()

books = Table(
    'books', meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('year', Integer),
)

meta.create_all(engine)

# INSERAREA DATELOR IN PROGRAM

conn = engine.connect()
query = books.insert()
query = books.insert().values(title = 'Dopamina', 
                               year = 2019)
conn = engine.connect()
result = conn.execute(query)


conn.execute(books.insert(), [
   {'title':'Dragostea in vremea holerei', 'year' : 2014},
   {'title':'Dante\'s Inferno', 'year' : 2012},
   {'title':'Why I Am so Clever', 'year' : 2016},
])

# AFISAREA DATELOR 

query = books.select()
conn = engine.connect()
result = conn.execute(query)

for row in result:
    print(row)