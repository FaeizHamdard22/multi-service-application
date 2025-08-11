from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# اتصال به PostgreSQL
db_conn = psycopg2.connect(
    host=os.environ.get("POSTGRES_HOST", "db"),
    database=os.environ.get("POSTGRES_DB", "mydb"),
    user=os.environ.get("POSTGRES_USER", "postgres"),
    password=os.environ.get("POSTGRES_PASSWORD", "example")
)

# اتصال به Redis
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask + Postgres + Redis"})

@app.route("/db")
def db_data():
    cur = db_conn.cursor()
    cur.execute("SELECT NOW();")
    now = cur.fetchone()
    cur.close()
    return jsonify({"db_time": str(now[0])})

@app.route("/cache")
def cache():
    r.set("greeting", "Hello from Redis")
    return jsonify({"cached_value": r.get("greeting").decode("utf-8")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
