# Basics

## Installation and setup

### Creating a Bot Account 

1. log in to ![discord website](https://discord.com/)
2. Navigate to the application page
3. Click on the new application button 
4. Give your application a name and then click on the create button 
5. Go to the bot tab and then click on *add bot*.
6. Save your token to a save place (DONT SHARE IT).

### Add it to your server 

1. Go to the *0Auth2* tab.
2. Tick the *bot* checkbox under the scopes 
3. Tick the permissions you want to give your bot 
4. Now paste the resulting url in a new tab of the browser and choose the server where you want to add the bot

## Startup bot

```
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
```

what is going on in the above program.
1. First line is simply importing the discord.py library in the file 
2. The second line is creating an instance of client which is simply a connection with the discord
3. `Client.event()` is used to register an event. The discord library is asynchronous there we use a callback style. A **callback** is essentially a function that is called when something happens. 
	- `on_ready()` event is called when the bot has finished logging in and settings things up 
	- `on_message()`  event is called when the bot has recieved a message.
*note: since on_message() activates on every message, we ignore the messages from ourselves. We do this by checking if the **Message.author** is the same as **Client.user**.
4. If the *message* starts with *$hello*, the bot will respond back with a *Hello!*
5. `Client.run(token)` will start the bot.

	
## Some Important async functions:

1. `on_member_join(member)` --> When a member joins, do.....
2. `on_member_remove(member)` --> When a member leaves (or is removed), do...
3. `on_ready()` --> When the bot is setup
4. `on_message(message)` --> When there is a message 