'''Using Selenium in headless mode to access youtube comments'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from models import ChatMessage, Base
from sqlalchemy.sql import exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
        
from time import sleep
import sys
import os

DB = "livechat.db"
REFRESH_RATE = 10 # seconds

engine = create_engine(f'sqlite:///{DB}')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)



# setup driver
chrome_options = Options()
chrome_options.add_argument("--headless")
# headless mode needs a user-agent tag otherwise yt thinks its an old browser
chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)


#TODO dynamically grab this from channel using YouTube API
base_url = "https://www.youtube.com/live_chat?v="
chat_id = "bfGaUembwA8"
url = base_url + str(chat_id)

def get_current_messages(url):
    "return a list of yt-live-chat-text-message-renderer elements"
    driver.get(url)
    chat_messages = driver.find_element_by_id('chat-messages')
    item_list = chat_messages.find_element_by_id('item-list')
    item = item_list.find_element_by_id('items')
    messages = item.find_elements_by_tag_name('yt-live-chat-text-message-renderer')
    return messages

def add_messages(url):
    "add messages to db if they aren't added"
    session = Session()
    messages = get_current_messages(url)
    for message_elem in messages:
        message = ChatMessage()
        message.author = message_elem.find_element_by_id('author-name').text
        message.text = message_elem.find_element_by_id('message').text
        message.message_id = message_elem.get_attribute('id')
        message_exists = session.query(exists().where(ChatMessage.message_id == message.message_id)).scalar()
        if not message_exists:
            try:
                session.add(message)
                session.commit()
                print("{}: {}".format(message.author, message.text))
            except:
                pass
    session.close()

while True:
	try:
		add_messages(url)
		sleep(REFRESH_RATE)
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			driver.quit()
			sys.exit(0)
		except SystemExit:
			os._exit(0)
