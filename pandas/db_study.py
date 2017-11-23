from db import DB 

database = DB(filename='logs.sqlite3', dbtype="sqlite")

print(database.tables)

log_df = database.tables.log 
print(log_df)
print(log_df.all())

print("\n\nQUERY with WHERE")
log_df = database.query('SELECT * FROM log WHERE user_id = 3')
print(log_df)