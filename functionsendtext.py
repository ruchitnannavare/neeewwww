import requests
from requests import ConnectionError
import json
from tkinter import messagebox
def custom_text(chat_id, text):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    message = "&text=" + str(text) + "\nregards, \nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message_request = url + bot_key + method + str(chat_id) + message
    requests.get(message_request)

def admission_successful(chat_id, name):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    text = f"Congratulations! {name}'s admission to Bhavik Patel's chemistry tuitions is successful. We will be sending texts through this Telegram account.\nHave a nice day," + "\nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message = "&text=" + str(text)
    message_request = url + bot_key + method + str(chat_id) + message
    requests.get(message_request)

def send_them_scores(name, score, maxscore, subject, date, g_cid, s_cid):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    text = f"{name} has scored {score} out of {maxscore} in {subject} test taken on {date}\nScore = {score}/{maxscore}.\nHave a nice day," + "\nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message = "&text=" + str(text)
    message_request_g = url + bot_key + method + str(g_cid) + message
    message_request_s = url + bot_key + method + str(s_cid) + message
    requests.get(message_request_g)
    requests.get(message_request_s)


imgbb_key = "55e466ac52f4e78ebb5fc3f0f00c765c"


"""
def send_bar_parent(bar_image, g_cid):
    imgbb_request = f"https://api.imgbb.com/1/upload?expiration=60&key={imgbb_key}"
    payload = {"image": open(bar_image, "rb")}
    imgbb_return = requests.post(imgbb_request, files=payload)
    img_data = json.loads(imgbb_return.content)
    bot.send_photo(g_cid, img_data["data"]["url_viewer"], caption="Result Bar")"""

def send_pie_parent_both(bar_image, g_cid, s_cid):
    if g_cid != None or s_cid != None:
        url = "http://api.telegram.org/bot"
        bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
        method = "/SendPhoto?chat_id="

        imgbb_request = f"https://api.imgbb.com/1/upload?expiration=240&key={imgbb_key}"
        payload = {"image": open(bar_image, "rb")}
        imgbb_return = requests.post(imgbb_request, files=payload)
        img_data = json.loads(imgbb_return.content)
        image_url = img_data["data"]["url_viewer"]
        caption = "Green colored slice indicates ward secured percentage between 75-100%.\nYellow colored slice indicates ward secured percentage between 50-74%.\norange colored slice indicates ward secured percentage between 25-49%.\nRed colored slice indicates, ward secured percentage between 0-25%.\nBlack colored slice indicates that your  ward was absent when the test was conducted.\n"

        message_request_g = url + bot_key + method + str(g_cid) + "&photo=" + image_url + "&caption=" + caption
        message_request_s = url + bot_key + method + str(s_cid) + "&photo=" + image_url + "&caption=" + caption

        requests.get(message_request_g)
        requests.get(message_request_s)

        #bot.send_photo(g_cid, img_data["data"]["url_viewer"], caption="Green colored slice indicates ward secured percentage between 75-100%.\nYellow colored slice indicates ward secured percentage between 50-74%.\norange colored slice indicates ward secured percentage between 25-49%.\nRed colored slice indicates, ward secured percentage between 0-25%.\nBlack colored slice indicates that your  ward was absent when the test was conducted.\n")
        #bot.send_photo(s_cid, img_data["data"]["url_viewer"], caption="Green colored slice indicates ward secured percentage between 75-100%.\nYellow colored slice indicates ward secured percentage between 50-74%.\norange colored slice indicates ward secured percentage between 25-49%.\nRed colored slice indicates, ward secured percentage between 0-25%.\nBlack colored slice indicates that your  ward was absent when the test was conducted.\n")

#message_request_g = url + bot_key + method + str(1212836306) + "&photo=" + image_url + "&caption=hello"


    else:
        return

def send_bar_parent_both(bar_image, g_cid, s_cid):
    if g_cid != None or s_cid != None:
        url = "http://api.telegram.org/bot"
        bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
        method = "/SendPhoto?chat_id="



        imgbb_request = f"https://api.imgbb.com/1/upload?expiration=240&key={imgbb_key}"
        payload = {"image": open(bar_image, "rb")}
        imgbb_return = requests.post(imgbb_request, files=payload)
        img_data = json.loads(imgbb_return.content)
        image_url = img_data["data"]["url_viewer"]
        caption = "Green colored bars indicates ward secured percentage between 75-100%.\nYellow colored bars indicates ward secured percentage between 50-74%.\norange colored bars indicates ward secured percentage between 25-49%.\nRed colored bars indicates, ward secured percentage between 0-25%.\nNO BAR indicates that your  ward was absent when the test was conducted.\n"

        message_request_g = url + bot_key + method + str(g_cid) + "&photo=" + image_url + "&caption=" + caption
        message_request_s = url + bot_key + method + str(s_cid) + "&photo=" + image_url + "&caption=" + caption

        requests.get(message_request_g)
        requests.get(message_request_s)

        #bot.send_photo(g_cid, img_data["data"]["url_viewer"], caption="Green colored bars indicates ward secured percentage between 75-100%.\nYellow colored bars indicates ward secured percentage between 50-74%.\norange colored bars indicates ward secured percentage between 25-49%.\nRed colored bars indicates, ward secured percentage between 0-25%.\nNO BAR indicates that your  ward was absent when the test was conducted.\n")
        #bot.send_photo(s_cid, img_data["data"]["url_viewer"], caption="Green colored bars indicates ward secured percentage between 75-100%.\nYellow colored bars indicates ward secured percentage between 50-74%.\norange colored bars indicates ward secured percentage between 25-49%.\nRed colored bars indicates, ward secured percentage between 0-25%.\nNO BAR indicates that your  ward was absent when the test was conducted.\n")
    else:
        return
