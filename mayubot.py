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
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler
from datetime import time
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def morning(bot, job):
    """Send the alarm message."""
    sticker = "CAADBQADShAAAsZRxhVwz5UcI85BmQI"
    bot.send_sticker(job.context, sticker)
    bot.send_message(job.context, text='Too-too-roo!')


def set_weeb_message(bot, update, args, job_queue, chat_data):
    """Add a job to the queue."""
    chat_id = "-1001092305384"
    sticker = "CAADBQADShAAAsZRxhVwz5UcI85BmQI"
    eightAm = time(hour = 8)
    # Add job to queue
    job = job_queue.run_daily(morning, eightAm, context=chat_id)
    chat_data['job'] = job

    update.message.reply_text('Alright you stupid noob')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater("652731656:AAHu8RhL9yo1lVuUnXN6kL2vEqFEz-NW5M4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("start", set_weeb_message,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

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