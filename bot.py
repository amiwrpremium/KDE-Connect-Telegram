#!/usr/bin/env python3

from myCommands import *
from config import *

from os import system, popen, mkdir, path
from datetime import datetime
from time import sleep

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import error

ADMIN: int = ADMIN_USERID

HOME_DIR = path.expanduser("~")
APP_PATH = f"{HOME_DIR}/KDE_Connect_Telegram"
PIC_PATH = f'{APP_PATH}/Pictures'
VIDEO_PATH = f'{APP_PATH}/Videos'
FILE_PATH = f'{APP_PATH}/Documents'
VOICE_PATH = f'{APP_PATH}/Voices'
AUDIO_PATH = f'{APP_PATH}/Audios'


def dir_maker(folder_name: str):
    if not path.isdir(f"{APP_PATH}/{folder_name}"):
        mkdir(f"{APP_PATH}/{folder_name}")


def passer(uid: int):
    if uid == ADMIN:
        return True
    else:
        return False


class Keyboards:
    def __init__(self):
        self.home_keyboard = [
            ['🎛️ States', '⚡️ Bluetooth'],
            ['💡 Brightness', '🔈 Volume'],
            ['📸 Screenshot', '⚙️ Utilities']
        ]
        self.home_markup = ReplyKeyboardMarkup(self.home_keyboard)

        self.states_keyboard = [
            ['📴 Shutdown', '🔄 Reboot'],
            ['⏸️ Suspend', '💤 Hibernate'],
            ['🔒 Lock Screen', '🔓Unlock Screen'],
            ['⚪ ️Screen On', '⚫️ Screen Off'],
            ['🔒 Lock keyboard & Mouse', '🔓Unlock keyboard & Mouse'],
            ['🏠 Home'],
        ]
        self.states_markup = ReplyKeyboardMarkup(self.states_keyboard, resize_keyboard=True)

        self.brightness_keyboard = [
            ['🔆 Up', '🔅 Down'],
            ['📈 Maximum'],
            ['🏠 Home']
        ]
        self.brightness_markup = ReplyKeyboardMarkup(self.brightness_keyboard, one_time_keyboard=False)

        self.volume_keyboard = [
            ['🔊 Up', '🔉 Down'],
            ['🔇 Mute', '🎙 Mute Mic'],
            ['🏠 Home']
        ]
        self.volume_markup = ReplyKeyboardMarkup(self.volume_keyboard, one_time_keyboard=False)

        self.screenshot_keyboard = [
            ['📸 Fullscreen', '📸 Active window'],
            ['📸 Fullscreen Here', '📸 Active window Here'],
            ['🏠 Home']
        ]
        self.screenshot_markup = ReplyKeyboardMarkup(self.screenshot_keyboard, one_time_keyboard=False)


keyboards = Keyboards()


class Bot:
    def __init__(self):
        self.main()

    @staticmethod
    def start_command(update: Update, context: CallbackContext) -> None:
        if passer(update.message.from_user.id):
            update.message.reply_text('Welcome Boss', reply_markup=keyboards.home_markup)
        else:
            update.message.reply_text('Fuck Off')
        return

    @staticmethod
    def states(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('🔹 Choose One 🔹', reply_markup=keyboards.states_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def shutdown(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                [
                    InlineKeyboardButton("✅ Yea", callback_data='YES SHUTDOWN'),
                    InlineKeyboardButton('❌ No', callback_data="NO SHUTDOWN")
                ]
            ]
            update.message.reply_text(
                'Are You Sure You Want To Shutdown?',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def reboot(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                [
                    InlineKeyboardButton("✅ Yea", callback_data='YES REBOOT'),
                    InlineKeyboardButton('❌ No', callback_data="NO REBOOT")
                ]
            ]
            update.message.reply_text(
                'Are You Sure You Want To Reboot?',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def suspend(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Suspended', reply_markup=keyboards.states_markup)
            system(Suspend)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def hibernate(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Hibernated', reply_markup=keyboards.states_markup)
            system(Hibernate)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def lock_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Locked', reply_markup=keyboards.states_markup)
            system(Lock_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def unlock_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Unlocked', reply_markup=keyboards.states_markup)
            system(Unlock_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def turn_off_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Turned Off', reply_markup=keyboards.states_markup)
            system(Turn_off_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def turn_on_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Turned On', reply_markup=keyboards.states_markup)
            system(Turn_on_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def lock_keyboard_and_mouse(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Keyboard & Mouse Locked', reply_markup=keyboards.states_markup)
            system(Lock_keyboard_and_mouse)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def unlock_keyboard_and_mouse(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Keyboard & Mouse Unlocked', reply_markup=keyboards.states_markup)
            system(Unlock_keyboard_and_mouse)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def bluetooth(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                ['Connect', 'Disconnect'],
                ['Pair', 'Remove']
            ]
            update.message.reply_text('🔹 Choose One 🔹',
                                      reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Up And Down', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_up(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Up)
            update.message.reply_text('🔆 Brightness Increased', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_down(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Down)
            update.message.reply_text('🔅 Brightness Decreased', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_max(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Maximum)
            update.message.reply_text('📈 Maximum Brightness', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Up And Down', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume_up(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Volume_up)
            update.message.reply_text('🔊 Volume Increased', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume_down(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Volume_down)
            update.message.reply_text('🔉 Volume Decreased', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def mute(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Mute)
            update.message.reply_text('🔇 Muted', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def mute_mic(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Mute_microphone)
            update.message.reply_text('🎙 Microphone Muted', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screenshot(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('🔹 Choose One 🔹',
                                      reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_fullscreen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(f'spectacle -b')
            update.message.reply_text('Captured', reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_active(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(f'spectacle -a -b')
            update.message.reply_text('Captured', reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_fullscreen_to_phone(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            file_name = f"/home/amiwr/Pictures/Screenshot/Screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            system(f'spectacle -b -n -o {file_name}')
            sleep(0.5)
            update.message.reply_photo(photo=open(file_name, 'rb'),
                                       caption=str(file_name),
                                       reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_active_to_phone(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            file_name = f"/home/amiwr/Pictures/Screenshot/Screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            system(f'spectacle -a -n -b -o {file_name}')
            sleep(0.5)
            update.message.reply_photo(photo=open(file_name, 'rb'),
                                       caption=str(file_name),
                                       reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def button(update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        chose = query.data

        if chose == 'YES SHUTDOWN':
            query.edit_message_text('Hope You Thought This Through!\n\n'
                                    '✅ Shutting Down...')
            system(Shutdown)
        if chose == 'NO SHUTDOWN':
            query.edit_message_text('❌ Canceled')
        if chose == 'YES REBOOT':
            query.edit_message_text('Hope You Thought This Through!\n\n'
                                    '✅ Rebooting...')
            system(Reboot)
        if chose == 'NO REBOOT':
            query.edit_message_text('❌ Canceled')

    @staticmethod
    def photo(update: Update, context: CallbackContext):
        media = update.message.photo[-1].file_id
        pic_file = context.bot.getFile(media)
        if not path.isdir(f"{APP_PATH}/Pictures"):
            mkdir(f"{APP_PATH}/Pictures")
        pic_file.download(f"/home/amiwr/Pictures/")

    def main(self):
        updater = Updater(TOKEN, use_context=True)
        dpa = updater.dispatcher.add_handler

        dpa(CommandHandler('start', self.start_command))

        dpa(MessageHandler(Filters.regex('^🏠 Home$'), self.start_command))

        dpa(MessageHandler(Filters.regex('^🎛️ States$'), self.states))
        dpa(MessageHandler(Filters.regex('^📴 Shutdown$'), self.shutdown))
        dpa(MessageHandler(Filters.regex('^🔄 Reboot$'), self.reboot))
        dpa(MessageHandler(Filters.regex('^⏸️ Suspend$'), self.suspend))
        dpa(MessageHandler(Filters.regex('^💤 Hibernate$'), self.hibernate))
        dpa(MessageHandler(Filters.regex('^🔒 Lock Screen$'), self.lock_screen))
        dpa(MessageHandler(Filters.regex('^🔓 Unlock Screen$'), self.unlock_screen))
        dpa(MessageHandler(Filters.regex('^⚪ ️Screen On$'), self.turn_on_screen))
        dpa(MessageHandler(Filters.regex('^⚫️ Screen Off$'), self.turn_off_screen))
        dpa(MessageHandler(Filters.regex('^🔒 Lock keyboard & Mouse$'), self.lock_keyboard_and_mouse))
        dpa(MessageHandler(Filters.regex('^🔓 Unlock keyboard & Mouse$'), self.unlock_keyboard_and_mouse))

        dpa(MessageHandler(Filters.regex('^⚡️ Bluetooth$'), self.bluetooth))

        dpa(MessageHandler(Filters.regex('^💡 Brightness$'), self.brightness))
        dpa(MessageHandler(Filters.regex('^🔆 Up$'), self.brightness_up))
        dpa(MessageHandler(Filters.regex('^🔅 Down$'), self.brightness_down))
        dpa(MessageHandler(Filters.regex('^📈 Maximum$'), self.brightness_down))

        dpa(MessageHandler(Filters.regex('^🔈 Volume$'), self.volume))
        dpa(MessageHandler(Filters.regex('^🔊 Up$'), self.volume_up))
        dpa(MessageHandler(Filters.regex('^🔉 Down$'), self.volume_down))
        dpa(MessageHandler(Filters.regex('^🔇 Mute$'), self.mute))
        dpa(MessageHandler(Filters.regex('^🎙 Mute Mic$'), self.mute_mic))

        dpa(MessageHandler(Filters.regex('^📸 Screenshot$'), self.screenshot))
        dpa(MessageHandler(Filters.regex('^📸 Fullscreen$'), self.screen_shot_fullscreen))
        dpa(MessageHandler(Filters.regex('^📸 Active window$'), self.screen_shot_active))
        dpa(MessageHandler(Filters.regex('^📸 Fullscreen Here$'), self.screen_shot_fullscreen_to_phone))
        dpa(MessageHandler(Filters.regex('^📸 Active window Here$'), self.screen_shot_active_to_phone))

        dpa(CallbackQueryHandler(self.button))

        dpa(MessageHandler(Filters.photo, self.photo))

        updater.start_polling()
        updater.idle()


def main():
    try:
        Bot()
    except error.TimedOut:
        print('Exception 1')
        main()
    except error.NetworkError:
        print('Exception 2')
        main()


if __name__ == '__main__':
    try:
        main()
    except error.TimedOut:
        print('Exception 3')
        main()
    except error.NetworkError:
        print('Exception 4')
        main()


# TODO Add notification sender
# TODO Add speed test
# TODO Add File Download (Filters.video save to vids and ...)
# TODO Add Battery Percentage
