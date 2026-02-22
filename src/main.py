import time
import config
from whatsapp_driver import WhatsAppBot
from ai_engine import generate_reply

processed_messages = {}

def main():
    bot = WhatsAppBot()
    while True:
        opened_chat = bot.get_active_chat_name()
        print("Chatting to:", opened_chat)

        if opened_chat == "UNKNOWN":
            reply = "Will buzz you shortly!"
        else:
            message = bot.get_last_incoming_message()
            print("Last message:", message)

            if not message:
                continue
            if message in processed_messages:
                continue
            reply = generate_reply(message)
            print("Bot reply:", reply)

        bot.send_message(reply)
        processed_messages[message] = True

        time.sleep(config.POLL_INTERVAL)

if __name__ == "__main__":
    main()
