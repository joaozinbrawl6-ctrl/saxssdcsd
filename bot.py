# saxssdcsdimport telebot
from telebot import types

TOKEN = "8398411787:AAFdnFHGrwFoEz0hNa7Qo2sLRKQMrXMUACo"
PIX_KEY = "joaozinbrawl6@gmail.com"
ADMIN_ID = 5524093272

GROUPS = {
    "variedades": "https://t.me/+2oqbp-UdEKg0YzEx",
    "gold": "https://t.me/+TF8V8GQIk8MxZDAx",
    "diamond": "https://t.me/+OvtNc2CTAhQ0Yzk5"
}

bot = telebot.TeleBot(TOKEN)
payments = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bem-vindo ao ZK HOT CLUB 🔥\nUse /vip para ver os planos disponíveis.")

@bot.message_handler(commands=['vip'])
def show_vip(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔥 Variedades", callback_data="variedades"))
    markup.add(types.InlineKeyboardButton("💎 Exclusivo Gold", callback_data="gold"))
    markup.add(types.InlineKeyboardButton("👑 Exclusivo Diamond", callback_data="diamond"))
    bot.send_message(message.chat.id, "Escolha seu nível VIP:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in GROUPS)
def ask_payment(call):
    plan = call.data
    payments[call.from_user.id] = plan
    bot.send_message(call.from_user.id,
                     f"Para acessar o plano {plan.upper()}, envie o valor via PIX:\n\n"
                     f"💳 Chave PIX: {PIX_KEY}\n\n"
                     f"Após pagar, envie /confirmar para solicitar aprovação.")

@bot.message_handler(commands=['confirmar'])
def confirm_payment(message):
    if message.from_user.id not in payments:
        bot.send_message(message.chat.id, "Você ainda não escolheu um plano. Use /vip primeiro.")
        return
    plan = payments[message.from_user.id]
    bot.send_message(ADMIN_ID, f"Usuário @{message.from_user.username} solicitou acesso ao plano {plan}.\n\n"
                               f"Aprovar? Use /aprovar {message.from_user.id}")
    bot.send_message(message.chat.id, "Pagamento enviado para análise.")

@bot.message_handler(commands=['aprovar'])
def approve(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "Você não tem permissão para isso.")
        return
    try:
        user_id = int(message.text.split()[1])
        plan = payments.get(user_id)
        if not plan:
            bot.send_message(message.chat.id, "Plano não encontrado para este usuário.")
            return
        bot.send_message(user_id, f"Aprovado ✅\nAcesse seu grupo: {GROUPS[plan]}")
        del payments[user_id]
        bot.send_message(message.chat.id, "Usuário aprovado com sucesso.")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Use: /aprovar ID_DO_USUÁRIO")

bot.polling()
worker: python bot.py
# 🤖 Bot ZK HOT CLUB

Bot de vendas VIP para Telegram com aprovação manual e integração com PIX.

## 📌 Como subir no Railway

### 1. Criar repositório no GitHub
1. Acesse [GitHub](https://github.com) e crie uma conta.
2. Clique em **New Repository** e crie um repositório público chamado `zk-hot-club-bot`.
3. Envie (`commit`) os arquivos deste projeto (`bot.py`, `requirements.txt`, `Procfile`).

### 2. Conectar no Railway
1. Vá para [Railway](https://railway.app) e crie uma conta.
2. Clique em **New Project → Deploy from GitHub**.
3. Conecte sua conta do GitHub ao Railway.
4. Escolha o repositório `zk-hot-club-bot`.
5. Aguarde o deploy (Railway instala as dependências automaticamente).

### 3. Rodar 24h
O Railway vai iniciar o bot e mantê-lo online 24h por dia.

---

💳 **Chave PIX:** `joaozinbrawl6@gmail.com`
👑 **Admin ID:** `5524093272`

Comando de admin:
```
/aprovar <id_usuario>
```

---

    

