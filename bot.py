import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot Token එක මෙතනට දාන්න
BOT_TOKEN = "2202407747:AAFw1Vls7wiB_I5zp77vYdV5WMkekXkJOxU"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ආයුබෝවන්! මට ඕනෑම ෆිල්ම් එකක් හෝ ෆයිල් එකක් එවන්න. මම ඒකට Direct Link එකක් හදලා දෙන්නම්.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.document.file_id
    file_name = update.message.document.file_name
    
    new_file = await context.bot.get_file(file_id)
    direct_link = new_file.file_path
    
    msg = f"🎬 **File Name:** {file_name}\n\n🔗 **Direct Link:**\n`{direct_link}`\n\n(මේ ලින්ක් එක ඔයාගේ සයිට් එකේ ප්ලේයර් එකට දාන්න පුළුවන්)"
    await update.message.reply_text(msg, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
