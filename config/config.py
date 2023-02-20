import logging

from aiogram import types
from decouple import config

from handlers.accounts import register as reg_accounts
from handlers.commands import register as reg_commands
from handlers.content_text import register as reg_content_text
from handlers.help import register as reg_help
from handlers.trading import register as reg_trading
from handlers.referrals import register as reg_referrals
from handlers.alert import register as reg_alert
from handlers.orders import register as reg_orders
from handlers.notifications import register as reg_notifications
bot_token = config("BOT_TOKEN")
logger = logging.getLogger(__name__)


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")
    ])


def register_handlers(dp):
    reg_accounts(dp)
    reg_commands(dp)
    reg_content_text(dp)
    reg_help(dp)
    reg_trading(dp)
    reg_referrals(dp)
    reg_alert(dp)
    reg_orders(dp)
    reg_notifications(dp)
