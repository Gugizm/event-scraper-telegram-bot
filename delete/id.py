from telegram.ext import Updater, CommandHandler
from telegram import Bot

# Define a command to get the group ID
def get_group_id(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=f"The ID of this group is: {chat_id}")

def main():
    # Create a bot instance with your bot token
    bot_token = '6976493225:AAF4TlVvfyEGMymsNZ8jgW2SxYM_mnRZx94'  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot = Bot(token=bot_token)

    # Initialize the updater
    updater = Updater(bot=bot)

    # Add a command handler for the /get_group_id command directly to the updater
    updater.dispatcher.add_handler(CommandHandler('get_group_id', get_group_id))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()