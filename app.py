import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # 作品集首頁內容
    return jsonify({
        "status": "success",
        "message": "歡迎來到我的 Python 後端作品集！",
        "owner": "你的名字"
    })

if __name__ == '__main__':
    # 關鍵：雲端平台會動態分配 Port，必須讀取環境變數
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)