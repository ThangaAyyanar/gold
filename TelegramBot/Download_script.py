#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple Telegram bot in which you can pass the url to the download the computer will download for you
# Reference : https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples
# My Blog : Thangaayyanar.blogspot.in

from telegram.ext import Updater, CommandHandler
import logging
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi! Use /download <download url> to download the file')


def initiate_download(bot, update, args, job_queue, chat_data):
    
    chat_id = update.message.chat_id
    
    try:
	    
      command = "wget " + args[0] + "&"
	    os.system(command)
      update.message.reply_text('Download process started')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /download <download url>')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater("<<Your Bot Id>>")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("download", initiate_download,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
	main()
