import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Secure Whitelist - Only IDs in this list can interact with the bot
AUTHORIZED_USERS = os.environ.get("TELEGRAM_AUTHORIZED_USERS", "").split(',')

async def verify_user(update: Update) -> bool:
    user_id = str(update.effective_user.id)
    if user_id not in AUTHORIZED_USERS:
        logging.warning(f"Unauthorized access attempt from user: {user_id}")
        await update.message.reply_text("Unauthorized access.")
        return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await verify_user(update): return
    await update.message.reply_text('Agent remote interface established. Standing by.')

async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Executes a command within the docker sandbox."""
    if not await verify_user(update): return
    
    cmd_args = context.args
    if not cmd_args:
        await update.message.reply_text("Usage: /exec <command>")
        return

    command = " ".join(cmd_args)
    await update.message.reply_text(f"Executing in sandbox: {command}")
    
    # In a full implementation, this triggers docker exec or similar
    # e.g. os.system(f"docker exec local-agent-sandbox {command}")
    await update.message.reply_text("[Simulated] Environment action logged.")

if __name__ == '__main__':
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("TELEGRAM_BOT_TOKEN not set. Exiting.")
        exit(1)
        
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("exec", execute_command))

    print("Starting Telegram Remote Interface...")
    app.run_polling()
