import random
import time
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def generate_reply(user_message):
    prompt = f"""
    You are
    polite,
    friendly,
    helpful,
    Funny.
    
    You are not
    always serious,
    always sweet.
    
    Keep it short and human-like.
    Do not use emojis. Use plain ASCII characters only.

    Message: {user_message}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print("bot generated response: ",response)
    reply = response.choices[0].message.content.strip()
    time.sleep(random.uniform(config.REPLY_DELAY_MIN, config.REPLY_DELAY_MAX))
    return reply
