from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from keep_alive import keep_alive
import random

BOT_TOKEN = "IL_TUO_TOKEN_QUI"
ALLOWED_CHAT_ID = None

TRIGGER_RESPONSE = {
    ("rosso", "rossi", "comunisti"): ["rossi di merda andate a fare in culo"],
    ("bambolina",): ["non capite un cazzo è bellissima", "ha un vestitino e una gonnellino che mi fa impazzire"],
    ("macchina", "automobile", "vettura"): ["la rav è nuova andate a cagare", "l'ho prestata per farle un piacere perchè ci tengo", "mi serve che devo portarle al mare"],
    ("europa", "comunità", "cee"): ["la von der Leyen è una pazza psicopatica", "vdl puttana di merda", "questa ci porta alla rovina totale"],
    ("filippo",): ["fa una pasta che non ti immagini"],
    ("cibo", "griglia", "grigliata", "mangiare", "cena", "pranzo"): ["andate a cagare che se non c'è roba abbastanza e resto con la fame poi mi incazzo"],
    ("telefono",): ["non scrivo nulla perché sono sottocontrollo", "non capite un cazzo, me lo hanno detto tutti che i telefoni sono clonati"]
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print("Chat ID:", chat_id)

    if ALLOWED_CHAT_ID and chat_id != ALLOWED_CHAT_ID:
        return

    text = update.message.text.lower()
    for keywords, responses in TRIGGER_RESPONSE.items():
        if any(word in text for word in keywords):
            await update.message.reply_text(random.choice(responses))
            return

if __name__ == '__main__':
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
