# Easy-to-Set-Up Discord Music Bot

This repository provides an easy-to-use solution for setting up and configuring a Discord music bot.
The bot supports both YouTube and Soundcloud platforms and can be further customized by adding new code and modules.

## **Table of contents** :

- [Requirments](#Requirments)
- [Setup instructions](#SetupInstructions)
  - [Windows](#Windows)
  - [Mac / Linux](#Mac/Linux)
- [Configuration Guide](#ConfigurationGuide)
- [Commands](#Commands)

<a name="Requirments"></a>

## **Requirments** :

- Python installed on your system ( [Download Python](https://www.python.org/downloads/) )
- A Discord bot account and token ( [Set up a discord bot account](https://discordpy.readthedocs.io/en/stable/discord.html) )

<a name="SetupInstructions"></a>

## **Setup Instructions** :

1. Clone this repository to a directory of your choice on your local system.
2. Navigate to the main folder and open the .env file.
3. In the .env file, add your bot token followed by your preferred prefix for bot commands (defaults to "&").
4. Save and close the .env file.
5. Follow the relevant instructions below based on your operating system.

<a name="Windows"></a>

### For windows users:

6. Run setup.bat located in the main directory.
7. Wait for the batch script to execute and close.
8. The setup process is complete. To start the bot, run start.bat.

<a name="Mac/Linux"></a>

### For mac / linux users:

6. Navigate to the "For-Mac" directory.
7. Execute Mac-setup.sh using the bash shell.
8. Wait for the script to complete.
9. The setup process is done. To start the bot, run start.sh.

<a name="Commands"></a>

## **Commands** :

- commandslist -- Displays a list of all music related commands
- status -- Displays the your bots current status

<a name="ConfigurationGuide"></a>

## **Configuration guide** :

Configuring your bot is a straightforward process. By creating your own modules and importing them as extensions in main.py or
editing the already existing modules, you can customize your bot's behavior.
Keep in mind to write and edit the code with regards to the Discord.py API reference.

Discord.py API reference: https://discordpy.readthedocs.io/en/stable/api.html
