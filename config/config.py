from decouple import config
import logging

from handlers.commands import register as reg_commands
from handlers.content_text import register as reg_content_text

bot_token = config("BOT_TOKEN")
logger = logging.getLogger(__name__)


def register_handlers(dp):
    reg_commands(dp)
    reg_content_text(dp)
