from typing import final
import logging
import tracemalloc
import asyncio
from telegram import Update, MenuButtonCommands
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
TOKEN : final = '8038816092:AAH4P4-KS33BU8hVAQwpjkGbFka49o_QN0M'
bot_username: final = '@JContractBot'

user_chat_id = [] 
user_name = []
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO

)



# Start tracemalloc to track memory allocations
tracemalloc.start()

# Replace 'YOUR_BOT_TOKEN' with your actual bot token

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_chat_id = update.effective_chat.id
    user_name = update.effective_user.first_name
    await update.message.reply_text(f'Hello {user_name} with the tag number of {user_chat_id}')

# Function to set up the menu button with predefined commands
async def setup_menu_button(application) -> None:
    commands = [
        {"command": "start", "description": "Welcome message"},
        {"command": "help", "description": "List of available commands"},
        {"command": "about", "description": "Information about the bot"},
        {"command": "contact", "description": "Contact information"},
    ]
    
    try:
        # Set the menu button to display commands
        await application.bot.set_my_menu_button(MenuButtonCommands(commands=commands))
        logging.info("Menu button set successfully.")
    except Exception as e:
        logging.error(f"Failed to set menu button: {e}")

# Main function to set up the bot handlers



if __name__ == '__main__':
    # Use asyncio to run the main coroutine
    application = ApplicationBuilder().token(TOKEN).build()

    # Set up the menu button configuration
    setup_menu_button(application)

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    
    # Run the bot
    application.run_polling()