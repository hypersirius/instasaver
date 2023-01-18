from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from telebot import TeleBot
from telebot.types import Message
from configs import *
import telebot
import requests
import time
# Открытие сайта входа в инстаграмм аккаунт
bot = TeleBot(TOKEN)
browser = webdriver.Firefox(executable_path='C:/Users/MODER/Desktop/Python/YouTube Bot/geckodriver')
browser.get('https://instagram.com')
time.sleep(2)
input_username = browser.find_element(By.NAME, 'username')
input_password = browser.find_element(By.NAME, 'password')
input_username.send_keys(username)
input_password.send_keys(password)
input_password.send_keys(Keys.ENTER)
user_link = []
# Ожидание комманды /start в боте


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Отправьте ссылку:')
    bot.register_next_step_handler(msg, inst)


def inst(message: Message):
    chat_id = message.chat.id
    link = message.text
    user_link = link
    browser.get(link)
    time.sleep(2)
    user_link = user_link.split('/')[-3]
    link = link.split('/')[-4]
    # Проверка ссылка на видео
    if 'reel' == user_link:
        tag = browser.find_element(By.TAG_NAME, 'video').get_attribute('src')
        response = requests.get(tag)
        print(tag)
        print(response)
        time.sleep(3)
        with open('video.mp4', 'wb') as video:
            video.write(response.content)
        video_file = open('video.mp4', 'rb')
        bot.send_video(chat_id, video_file)
    # except Exception as ex:
    #     print(ex)
    # Проверка ссылки на фото
    elif 'p' == user_link:
        time.sleep(1)
        buttonone = browser.find_element(By.CLASS_NAME, "_afxw")
        try:
            tag = browser.find_element(By.TAG_NAME, 'video').get_attribute('src')
            response = requests.get(tag)
            print(tag)
            print(response)
            time.sleep(3)
            with open('video.mp4', 'wb') as video:
                video.write(response.content)
            video_file = open('video.mp4', 'rb')
            bot.send_video(chat_id, video_file)
        except:
            try:
                bot.send_message(chat_id, 'Брат, не волнуйся ща отправлю')
                for i in range(10):
                    buttonone.click()
                    time.sleep(0.5)
                    tag = browser.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    response = requests.get(tag)
                    time.sleep(1)
                    with open('photo.jpg', 'wb') as img:
                        img.write(response.content)
                        time.sleep(0.5)
                    img_file = open('photo.jpg', 'rb')
                    bot.send_photo(chat_id, img_file)

                    time.sleep(1)
                    browser.find_element(By.CLASS_NAME, "_afxw")
            except:
                print('a')

    # elif 'stories' == link:
    #     button = browser.find_element(By.TAG_NAME, 'button')
    #     button.click()
    #     time.sleep(0.5)
    #     tag = browser.find_element(By.TAG_NAME, 'video').get_attribute('src')
    #     response = requests.get(tag)
    #     print(tag)
    #     print(response)
    #     time.sleep(3)
    #     with open('stories.mp4', 'wb') as stories:
    #         stories.write(response.content)
    #     stories_file = open('video.mp4', 'rb')
    #     bot.send_video(chat_id, stories_file)


    # try:
    #     tag = browser.find_element(By.TAG_NAME, 'img').get_attribute('src')
    #     response = requests.get(tag)
    #     time.sleep(1)
    #     with open('photo.jpg', 'wb') as img:
    #         img.write(response.content)
    #     img_file = open('photo.jpg', 'rb')
    #     bot.send_photo(chat_id, img_file)
    #     time.sleep(1)
    #         # button = browser.find_element(By.XPATH, "//button[aria-label('Далее')]")
    #         # button.cl

    # except Exception as ex:
    #     print(ex)

bot.polling(none_stop=True)