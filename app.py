from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # يسمح لـ GitHub Pages تتكلم مع السيرفر

@app.route('/check', methods=['POST'])
def check_username():
    data = request.get_json()
    username = data.get('username', '')

    url = "https://www.instagram.com/api/v1/users/check_username/"

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'x-ig-www-claim': "0",
        'x-requested-with': "XMLHttpRequest",
        'x-csrftoken': "XKTR39rx_lkeJ2nTEGG9eB",
        'x-ig-app-id': "1217981644879628",
        'x-instagram-ajax': "1015171929",
        'x-asbd-id': "129477",
        'origin': "https://www.instagram.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.instagram.com/accounts/signup/username/?hl=ar",
        'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    try:
        response = requests.post(
            url,
            params={'hl': 'ar'},
            data=f"username={username}",
            headers=headers,
            timeout=10
        )
        text = response.text
        available = 'true' in text.lower()
        return jsonify({ 'available': available, 'username': username })

    except Exception as e:
        return jsonify({ 'error': str(e) }), 500


@app.route('/')
def home():
    return "IG Checker API is running ✅"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
