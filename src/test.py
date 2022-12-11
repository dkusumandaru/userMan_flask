


from sqlalchemy import create_engine

engine = create_engine("mysql://root@localhost/perpustakaan_db")
con = engine.connect()


result = con.execute("SELECT * FROM librarian")

for data in result:
	print(data)