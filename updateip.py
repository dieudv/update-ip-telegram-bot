from configparser import ConfigParser
from requests import post, get

data = ConfigParser(comment_prefixes='/', allow_no_value=True)
data.read('data.ini')

apiURL = f'https://api.telegram.org/bot{data["main"]["bot_token"]}/sendMessage'

def send_to_telegram(message):
    try:
        post(apiURL, json={'chat_id': data["main"]["chat_id"], 'text': message})
    except Exception as e:
        print(e)

def save_changes_to_config():
    with open('data.ini', 'w') as data_file:
        data.write(data_file)

res = get('http://ifconfig.me/ip').text

if data["main"]["last_ip"] != res:
    data["main"]["last_ip"] = res
    send_to_telegram(data["main"]["last_ip"])
    save_changes_to_config()