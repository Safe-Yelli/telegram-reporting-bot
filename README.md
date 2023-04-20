# Intent
While this Telegram Bot is not operational yet, it intents to **streamline** the procedure to report a safety incident **anonymously*** into a single application (Telegram). It is a question-answer based text user interface, and aims to collect information about the incident including date, time, location, category, and description, in a **conversational manner** which is similar to chatting with a person on Telegram. The collected data is added to the database of incidents collected by [safeyelli.in](https://safeyelli.in/) and is used for safety analysis, and contributing to a better **understanding of the safety dynamics** of an area as well as to understand which parameters affect the safety.

_Anonymously* : The only user specific information that we can obtain is the User ID, which to my knowledge cannot be traced back to the Username on Telegram. I said "can obtain" because, though it is possible, we are not storing the User ID anywhere._

## Use Cases
- Reporting Incidents: Users can interact with the Telegram bot to report personal safety incidents that they have experienced. The **bot will prompt** them for information such as the date, time, location, category, and description of the incident, and collect the data in an anonymous manner.
- Anonymous Reporting: The bot ensures that all information is collected anonymously, without requiring any personal identification information, to protect the privacy and confidentiality of the users.

## Current Status
The bot is under development now. The aim is to make reporting as seamless as possible while making it empathetic in a way, so that users don't have to go through the same upsetting feelings while describing the incident. 

## Roadmap
- To provide the option of providing an address, which can then be geocoded, or allow location sharing.
- Geocoding addresses would possibly be inaccurate with numerous issues associated, this could be adopted a two pronged strategy, possibly providing both options, or by letting the user verify the geocoded location
- To give date and time prompt buttons to make number formats uniform. (dd mm yyyy, hh:mm)
- To make the conversation more empathetic in terms of language.

# How to contribute
### Getting Started Requirements 
- Refer to [Python Telegram Bot documentation](https://github.com/python-telegram-bot) for all possible features.
- ```pip install python-telegram-bot```
- Can use [Replit](https://replit.com/) to run the python code on a server and make the bot run 24x7.
- Telegram Bot Token: You will need a Telegram bot token to authenticate and interact with the Telegram API. You can generate a token by creating a new bot on Telegram using BotFather.
