#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Simple Bot to send timed Telegram messages.
# This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import requests
import re
import datetime
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def bop(update, context):
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def cat(update, context):
    contents = requests.get('https://theoldreader.com/kittens/600/400')
    url = contents.url
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def morning(update, context):
    """Send the alarm message."""
    sticker = "CAADBQADShAAAsZRxhVwz5UcI85BmQI"
    chat_id = update.message.chat_id
    context.bot.send_sticker(chat_id, sticker)
    context.bot.send_message(chat_id, text='Too-too-roo!')


def set_weeb_message(update, context, args, job_queue, chat_data):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    eightAm = datetime.time(hour = 14)
    # Add job to queue
    #job = job_queue.run_daily(morning, eightAm, context=chat_id)
    day = 1
    hours = 24*day
    minutes = 60 * hours
    seconds = 60 * minutes
    twice = seconds/2
    job = job_queue.run_repeating(morning, interval = seconds, first = eightAm, context = chat_id)
    chat_data['job'] = job


    job2 = job_queue.run_repeating(working, interval = 3600, first = 0, context = chat_id)
    chat_data['job2'] = job2


def time(update, context):
    rn = datetime.datetime.now().time()
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, text = str(rn))


def damn(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, text = "Truth hurts doesnt it")


def hellothere(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, text = "General Kenobi")

def help(update, context):
    chat_id = update.message.chat_id
    helpString = """Available Commands: \n
/hellothere
/cat
/bop 
/damn
/morning
/tragedy"""
    context.bot.send_message(chat_id, text = helpString)


def tragedy(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, text = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Run bot."""
    updater = Updater("652731656:AAHu8RhL9yo1lVuUnXN6kL2vEqFEz-NW5M4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("damn", damn))
    dp.add_handler(CommandHandler("morning", morning))
    dp.add_handler(CommandHandler("hellothere", hellothere))
    dp.add_handler(CommandHandler("tragedy", tragedy))
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('cat',cat))
    dp.add_handler(CommandHandler('help',help))




    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
