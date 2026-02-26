import zulip
from datetime import datetime
from zoneinfo import ZoneInfo

tz = ZoneInfo("Europe/London")
now = datetime.now(tz)

#if now.hour != 12:
#    exit()

client = zulip.Client(
    email="lunch-bot@oakleygroup.zulipchat.com",
    api_key="Mfy70yNDzTemShSL5vz9PtUVzPKEIM1k",
    site="https://oakleygroup.zulipchat.com",
)"

response = client.send_message({
    "type": "stream",
    "to": "general",        # Channel name
    "topic": "lunch",       # Topic name
    "content": "lunch in breakroom",
})
