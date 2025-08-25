from flask import Flask , render_template
import os
import redis
app = Flask(__name__)

# Get values from env variables
HELLO_MSG = os.getenv("HELLO_MSG", "Hello from flask!")
APP_PASSWORD = os.getenv("APP_PASSWORD", "admin123")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

#redis client
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.route("/")
def index():
    # Simple counter stored in Redis
    count = r.incr("hits")

    return render_template(
        "index.html",
        count=count,
        hello=HELLO_MSG,
        password=APP_PASSWORD  # just to *see* it in action
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)