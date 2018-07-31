import sqlite3

# Tabellennamen: ['wahlprogramme', 'bibel' 'maerchen' 'brk' 'nachrichten', 'buecher']
# Spaltennamen: ['pos', 'title', 'leicht', 'standard']
DBNAME = 'leichte_sprache.db'
TABLENAME = 'wahlprogramme'

conn = sqlite3.connect(DBNAME)

c = conn.cursor()

query = "SELECT * FROM {}".format(TABLENAME)
result = c.execute(query)

conn.commit()


for row in result:
	print(row)
	# break
	
conn.close()
