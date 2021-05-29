# Logging.py

*There can be some errors and debug information that can't be noticed without the logging python module.*

```
import logging

logging.basicConfig(level=logging.INFO)
```
This will output the logs from discord as well as other libraries that use the logging module directly to the console.

*Note:The optional **level** argument specifies what level of events to log out and can be any of **CRITICAL, ERROR, WARNING, INFO, and DEBUG** and if not specified `defaults to WARNING`.*

## To write logs in a file discord.log
```
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
```


