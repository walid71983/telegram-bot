import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8133599775:AAGddHyKnJtL2kzq4LmQVFANFUKq4KxNq2I"  # Replace with your BotFather token

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.reply("👋 Hello! Send me a photo and I will remove the background later ✨")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
