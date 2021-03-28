'''Using Selenium in headless mode to access youtube comments'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

# get the page and process the messages
driver.get(url)
chat_messages = driver.find_element_by_id('chat-messages')
item_list = chat_messages.find_element_by_id('item-list')
item = item_list.find_element_by_id('items')
messages = item.find_elements_by_tag_name('yt-live-chat-text-message-renderer')

for message in messages:
    author = message.find_element_by_id('author-name').text
    message = message.find_element_by_id('message').text
    print("{}: {}".format(author, message))

# close out
driver.quit()
