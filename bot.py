from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config.config as cfg
from database.mysql import user, user_exchange
import asyncio
import logging


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'[%(asctime)s] - %(message)s')
    cfg.logger.info("Starting bot")

    bot = Bot(cfg.bot_token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    cfg.register_handlers(dp)

    await user.connect_main()
    await user_exchange.connect_exchange()
    await cfg.set_default_commands(dp)
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
