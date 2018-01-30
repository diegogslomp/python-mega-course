import time
from datetime import datetime as dt

host_path=r"hosts"
redirect=r"127.0.0.1"
website_list=['www.facebook.com','facebook.com','dub119.mail.live.com','www.dub119.mail.live.com']

while True: 
    if dt.now().hour > 8 and dt.now().hour < 17:
        print('Working hours..')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        print('Not Working hours..')
        with open(host_path, 'r+') as file:
            content_list = file.readlines()
            file.seek(0)
            for line in content_list:
                if not any(website in line for website in website_list):
                        file.write(line)
            file.truncate()
    time.sleep(2)

