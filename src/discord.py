import os
import requests
from makeSentence import makeSentence

main_content = {
  "content": makeSentence()
}

requests.post(os.getenv("DISCORD_WEBHOOK_URL"), main_content)
