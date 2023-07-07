import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, functions

load_dotenv()

client = TelegramClient(
	os.environ.get('SESSION_NAME'),
	int(os.environ.get('APP_ID')),
	os.environ.get('APP_TOKEN'))

@client.on(events.NewMessage(
	chats=(os.environ.get('INPUT_CHANNEL'))
))
async def normal_handler(event):
	if (event.message.post == True):
		await client(functions.messages.ForwardMessagesRequest(
			from_peer = os.environ.get('INPUT_CHANNEL'),
			id = [event.message.id],
			to_peer = os.environ.get('OUTPUT_CHAT'),
			# For the chat-Forum
			top_msg_id = int(os.environ.get('OUTPUT_CHAT_THEME')),
			silent = bool(os.environ.get('SILENT')),
			background = bool(os.environ.get('BACKGROUND'))
		))

client.start()
client.run_until_disconnected()
