import os
import telebot
import requests

API_KEY = os.getenv('API_KEY')
listOfAllCentresFor45 = []
listOfAllCentresFor18 = []
bot = telebot.TeleBot('1814914546:AAHEqDamOm4Wm5vZoSQHeft-shsFbQ4R12g')
print("hello\n")


def init():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(
            message,
            "Howdy, how are you doing?\nyou can ask me for '/covid vaccine near me' or '/vaccine slot' , and i will serach it for you "
        )


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, message.text)
def slot_by_pin():
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.send_message(message.chat.id, message.text)
        print(message.text)
        if (message.text == '/exit'):
            print('-----flag_gen:1-----')
            init()

       
        
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=452001&date=19-06-2021")

        if (response.status_code != 200):
          print(response + "bad response")
          echo_all(message)

        # data = response.json()
        
        # data = json.loads(response.text)
        cnt1 = 1
        cnt2 = 1
        centre_detail_1 = ""
        centre_detail_2 = ""
        # data = json.dumps(data)
        for d in data["sessions"]:

          if d["min_age_limit"] == 45:
            centre_detail_1 =centre_detail_1 + "Centre {0}: ".format(cnt1)+ "nCentre Adrress:" 
            + d['name'] + ", " + d["address"] + "nVaccine: " + d['vaccine'] 
            + "nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) 
            + "nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + 'n'
            listOfAllCentresFor45.append(centre_detail_1)
            centre_detail_1=''
            cnt1=cnt1+1

          elif d["min_age_limit"] == 18:
            centre_detail_2 =centre_detail_2 + "Centre {0}: ".format(cnt2)+ "nCentre Adrress:" 
            + d['name'] + ", " + d["address"] + "nVaccine: " + d['vaccine'] 
            + "nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) 
            + "nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + 'n' 
            listOfAllCentresFor18.append(centre_detail_2)
            centre_detail_2=''
            cnt2=cnt2+1

        bot.send_message(message.chat.id, listOfAllCentresFor18)
        bot.send_message(message.chat.id, listOfAllCentresFor45)
        # print(json_response['sessions'])


@bot.message_handler(commands=[
    'vaccine', 'vaccine slot', 'covid vaccine near me ', 'vaccine near me'
])
def send_slot(message):
    a = message.text
    bot.reply_to(message, "don't worry ,i will search them for you ")
    print(a)
    bot.reply_to(message, "enter your address pin in this manner '/411040'")
    slot_by_pin()


init()
slot_by_pin()
bot.polling()
