import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # 預留：未來可以回傳 HTML 網頁 (如 index.html)
    return jsonify({
        "status": "success",
        "message": "Flask 作品集成功部署！"
    })

if __name__ == '__main__':
    # 雲端平台分配的 Port，找不到時（如本地測試）預設為 5000
    port = int(os.environ.get("PORT", 5000))
    # 必須綁定在 0.0.0.0，平台才能從外部對接流量
    app.run(host='0.0.0.0', port=port)