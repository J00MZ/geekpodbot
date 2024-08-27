from datetime import datetime as dt
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import requests
import json
from listennotes import podcast_api
import os
import logging
import coloredlogs

logger = logging.getLogger(__name__)
LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()
coloredlogs.install(level=LOGLEVEL)
TELEGRAM_TOKEN = os.getenv('TG_TOKEN')
LISTEN_NOTES_API_KEY = os.getenv('LISTEN_NOTES_API_KEY')
client = podcast_api.Client(api_key=LISTEN_NOTES_API_KEY)

async def start(update: Update, context):
    await update.message.reply_text('מה הפודקאסט שתרצה לשמוע?')

async def search_podcast(update: Update, context):
    query = update.message.text
    logger.info(f'Searching for podcast: {query}')
    response = client.search(
            q=query,
            sort_by_date=0,
            type='podcast',
            only_in='title,description',
            language='English,Hebrew',
            page_size=10,
        )
    results = response.json()['results']
    logger.info(f'Podcasts: {results}')
    if not results:
        await update.message.reply_text('לא נמצאו פודקאסטים שתואמים את החיפוש, נסה שוב עם שם פודקאסט אחר.')
        return
    
    keyboard = [
        [InlineKeyboardButton(podcast['title_original'], callback_data=podcast['id'])]
        for podcast in results
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('בחר פודקאסט:', reply_markup=reply_markup)

async def button(update: Update, context):
    query = update.callback_query
    podcast_id = query.data
    
    url = f'https://listen-api.listennotes.com/api/v2/podcasts/{podcast_id}'
    headers = {
        'X-ListenAPI-Key': LISTEN_NOTES_API_KEY
    }
    
    response = requests.get(url, headers=headers)
    episodes = response.json()['episodes']
    
    if not episodes:
        await query.edit_message_text('לא נמצאו פודקאסטים שתואמים את החיפוש, נסה שוב.')
        return
    
    keyboard = [
        [InlineKeyboardButton(episode['title'], callback_data=f"url_{episode['audio']}")]
        for episode in episodes
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text('בחר פרק:', reply_markup=reply_markup)

async def send_episode(update: Update, context):
    query = update.callback_query
    episode_url = query.data.split('_', 1)[1]
    logger.info(f'הורד את הפרק כאן: {episode_url}')
    # Send the audio file using the stored URL
    await context.bot.send_audio(chat_id=query.message.chat_id, audio=episode_url)

def main():
    application = Application.builder().token(token=TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('search', search_podcast))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(send_episode))
    
    application.run_polling()

if __name__ == '__main__':
    """
    Main function to start the bot.
    """
    logger.info('Starting bot... ')
    main()
