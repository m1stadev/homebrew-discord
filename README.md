# Homebrew-Discord
Homebrew-Discord is a bot I wrote out of boredom to fetch information on packages using the [Homebrew](https://brew.sh/) API.

Its current purpose is to downgrade devices (vulnerable to [checkm8](https://github.com/axi0mX/ipwndfu)) to previous iOS versions. However, there are other possible uses for this tool as well.

## Setup
To locally host, just follow these steps:
1. Install the required libraries:
`pip3 install -r requirements.txt`

2. Create a file named `token.txt`, that contains **only** your bot token.

3. Run `bot.py`:
`python3 bot.py`

## Live Demo
Homebrew-Discord can be invited into any Discord server using [this](https://discord.com/oauth2/authorize?client_id=767889324431376385&scope=bot&permissions=3072) link.