from fastapi import FastAPI
import uvicorn
import psycopg2
import os

app = FastAPI()
conn_str = os.environ["POSTGRES_CONNECTION_STRING"]
conn = psycopg2.connect(conn_str)
conn.autocommit = True
cur = conn.cursor()
# cur.execute("CREATE TABLE mytable (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO mytable (num, data) VALUES (%s, %s)", (100, "sto"))
@app.get("/")
def root():
    cur.execute("SELECT * FROM mytable")
    res = cur.fetchall()
    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
