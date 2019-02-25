# BroadcastTelegramBot
Python bot for broadcasting with options
Created by:
Abraham Arias and Pablo Rodriguez 2019
## Install

Dependencies:
    - python-telegram-bot 12.0.0b1

Just run:
```bash
pip install -r requirements.txt
```

and then build python-telegram-bot manually
```bash
git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
cd python-telegram-bot
python setup.py install
cd ..
rm -rf python-telegram-bot
```

Finally create telegram folder on home for persistancy
```bash
mkdir ~/telegram
```

## Usage
### Windows

```bash
$env:TELEGRAM_TOKEN = "secrettoken"
```

### Linux

```bash
export TELEGRAM_TOKEN = "secrettoken"
```