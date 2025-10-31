import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎉 البوت يعمل بنجاح!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('الأوامر: /start - /help')

def main():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        logging.error("❌ لم يتم تعيين BOT_TOKEN")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    logging.info("✅ البوت يعمل...")
    application.run_polling()

if __name__ == '__main__':
    main()
