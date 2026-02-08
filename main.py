from pyrogram import Client
from pyrogram.errors import FloodWait, UserPrivacyRestricted, PeerIdInvalid
import asyncio

api_id = 1488
api_hash = "14888"

chat_id = -100
text = "подпишись на @dev_zone"

app = Client("anal", api_id=api_id, api_hash=api_hash, test_mode=True)

async def send_all():
    async for member in app.get_chat_members(chat_id):
        user = member.user

        if user.is_bot:
            continue

        try:
            await app.send_message(user.id, text)
            print(f"Отправлено: {user.id}")
            await asyncio.sleep(1)

        except UserPrivacyRestricted:
            print(f"Закрытая личка: {user.id}")

        except PeerIdInvalid:
            print(f"Нельзя написать: {user.id}")

        except FloodWait as e:
            print(f"FloodWait {e.value} сек")
            await asyncio.sleep(e.value)

        except Exception as e:
            print(f"Ошибка {user.id}: {e}")

with app:
    app.loop.run_until_complete(send_all())
