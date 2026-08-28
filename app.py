import os
from flask import Flask, render_template

app = Flask(__name__)

# 確保這整個專案裡，只有一個 @app.route('/') 且只有一個 def home():
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)