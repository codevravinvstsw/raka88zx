import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import hmac
import hashlib
import json
from collections import namedtuple
from coinpayments import CoinPaymentsAPI
import time
import subprocess
import logging
import sys
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
import time
import os
import requests

ltcprice = requests.get('https://api.cryptonator.com/api/ticker/ltc-btc')
dogeprice = requests.get('https://api.cryptonator.com/api/ticker/doge-btc')
ethprice = requests.get('https://api.cryptonator.com/api/ticker/eth-btc')
bchprice = requests.get('https://api.cryptonator.com/api/ticker/bch-btc')
dashprice = requests.get('https://api.cryptonator.com/api/ticker/dash-btc')
zecprice = requests.get('https://api.cryptonator.com/api/ticker/zec-btc')
etcprice = requests.get('https://api.cryptonator.com/api/ticker/etc-btc')

get_lprice = ltcprice.json()
print("Name:", get_lprice['ticker']['price'])
get_dprice = dogeprice.json()
get_eprice = ethprice.json()
get_bprice = bchprice.json()
get_daprice = dashprice.json()
get_zprice = zecprice.json()
get_etprice = etcprice.json()

api = CoinPaymentsAPI(public_key='a0d8eb09688f0b074d2cfa89832b58535fdf5fc82d47bae90b5304c080c0e29c', private_key='77b1dc1711A5E077e1cbdCE5629353838849D9a2D549Cc6286b188525f256170')

bot = telebot.TeleBot('893429913:AAHY7B_9zqTjQwc0oH0zo7Tc7R9mOQL95SQ')
 


botadmin = 624816085
adminbot = 624816085
userStep = {}
passwd = ['word1234pass']
reflist = {}
nonref = []
user_list =[]
balance = {}
invest = {}
refbonus = {}
wrefbonus = {}
reinvest = {}
wdbal = {}
btcad = {}
ethad = {}
ltcad = {}
dogead = {}
bchad = {}
dashad = {}
etcad = {}
zecad = {}
adrqt = {}
witrqt = {}
wfa = {}
ptyid = []
key_bal = {}
rirqt = []
support_id = []
user_names = {}
tx_id = []
wda = {}
btcwad = {}
ltcwad = {}
dogewad = {}
ltc_price = []
doge_price = []
u_started = []

def sub_check(c_id):
     i = int(c_id)
     x = bot.get_chat_member("@CryptoHouse_Transactions", i).status
     if x == "left":
       bot.send_message(i, "Sorry.. You need to subscribe our channel: \nPublic Chat:\n@CryptoHouse_Chat\nTransactions: @CryptoHouse_Transactions", reply_markup=join_b)
     else:
       print(time.time())

commands = {
    'start'       : 'Get used to the bot', 
    'help'        : 'Gives you information about the available commands',
    'sendLongText': 'A test using the \'send_chat_action\' command',
    'getImage'    : 'A test using multi-stage messages, custom keyboard, and media sending'
}



def _json_hook(d): 
    return namedtuple('X', list(d.keys()))(*list(d.values()))

def pObject(data): 
    return json.loads(data, object_hook=_json_hook).result


class CryptoPayments():

        
    url = 'https://www.coinpayments.net/api.php'
    

    def __init__(self, publicKey, privateKey, ipn_url):
        self.publicKey = '0d809e3c5e587fd3c6acfe6bbceb525cd56803ce7063fe83572513711bed96b1'
        self.privateKey = '77618258Bd6b41d6d760c71A44D139dfCd1E97B855EB9CE10dA289daaf8dEb57'
        self.ipn_url = ipn_url
        self.format = 'json'
        self.version = 1

    def createHmac(self, **params):
        """ Generate an HMAC based upon the url arguments/parameters
            
            We generate the encoded url here and return it to Request because
            the hmac on both sides depends upon the order of the parameters, any
            change in the order and the hmacs wouldn't match
        """
        encoded = urllib.parse.urlencode(params).encode('utf-8')
        return encoded, hmac.new(bytearray(self.privateKey, 'utf-8'), encoded, hashlib.sha512).hexdigest()

    def Request(self, request_method, **params):
        """ The basic request that all API calls use
            the parameters are joined in the actual api methods so the parameter
            strings can be passed and merged inside those methods instead of the 
            request method. The final encoded URL and HMAC are generated here
        """
        encoded, sig = self.createHmac(**params)

        headers = {'hmac': sig}

        if request_method == 'get':
            req = urllib.request.Request(url, headers=headers)
        elif request_method == 'post':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            req = urllib.request.Request(self.url, data=encoded, headers=headers)

        try:
            response      = urllib.request.urlopen(req)
            status_code   = response.getcode()
            response_body = response.read()
        except urllib.error.HTTPError as e:
            status_code   = e.getcode()
            response_body = e.read()

        return pObject(response_body)


def gen_markup(ccid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 8
    markup.add(InlineKeyboardButton("Check Exchange Rates", callback_data=ccid))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data:
     cid = int(call.data)
     pl = get_lprice['ticker']['price']
     pe = get_eprice['ticker']['price']
     pd = get_dprice['ticker']['price']
     pb = get_bprice['ticker']['price']
     pda = get_daprice['ticker']['price']
     pz = get_zprice['ticker']['price']
     pet = get_etprice['ticker']['price']
     bot.send_message(cid, "LTC - *" + str(pl) + " BTC*\nETH -* " + str(pe) + " BTC*\nDOGE - *" + str(pd) + " BTC*\nBCH -* " + str(pb) + " BTC*\nDASH -* " + str(pda) + " BTC*\nZEC - *" + str(pz) + " BTC*\nETC - *" + str(pet) + " BTC*", parse_mode='Markdown')

menu2 = types.KeyboardButton('➕ Invest')
menu3 = types.KeyboardButton('🔃 Reinvest')
menu4 = types.KeyboardButton('➖ Withdraw')
menu5 = types.KeyboardButton('ℹ About')
menu6 = types.KeyboardButton('👥 Referrals')
menu7 = types.KeyboardButton('📞 Support')
menu8 = types.KeyboardButton('⬅️ Return') 
menu9 = types.KeyboardButton('BTC') 
menu10 = types.KeyboardButton('LTC') 
menu11 = types.KeyboardButton('DOGE') 
menu12 = types.KeyboardButton('ETH') 
menu13 = types.KeyboardButton('DASH') 
menu14 = types.KeyboardButton('BCH') 
menu15 = types.KeyboardButton('ZEC') 
menu16 = types.KeyboardButton('ETC') 
menu17 = types.KeyboardButton('Litecoin') 
menu18 = types.KeyboardButton('Dogecoin') 

join_b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
join_b.add('✅ Joined')

return_b = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
return_b.add('⬅️ Return')

menubal = types.ReplyKeyboardMarkup(resize_keyboard=True)
menubal.row(menu2, menu3)
menubal.row(menu4)
menubal.row(menu8)

investk = types.ReplyKeyboardMarkup(resize_keyboard=True)
investk.row(menu9, menu10, menu12, menu11)
investk.row(menu14, menu13, menu15, menu16)
investk.row(menu8)

pmethod = types.ReplyKeyboardMarkup(resize_keyboard=True)
pmethod.row(menu17, menu18)
pmethod.row(menu8)

hideBoard = types.ReplyKeyboardRemove()

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot.set_update_listener(listener) 

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


def in_storage(unique_code):
    return True



def get_username_from_storage(unique_code):
    return "ABC" if in_storage(unique_code) else None


def save_chat_id(chat_id, username):
    pass



@bot.message_handler(commands=['start'])
def send_welcome(m):
 cid = m.chat.id
 if cid not in user_list:
    user_names.update({cid: m.chat.first_name})
    j = float(0.00000000)
    balance.update({cid: j})
    invest.update({cid: j})
    refbonus.update({cid: j})
    reinvest.update({cid: j})
    wdbal.update({cid: j})
    key_bal.update({cid: str(0.00000000)})
    user_list.append(cid)
    userStep[cid] = 0
    unique_code = extract_unique_code(m.text)
    if unique_code:
        username = get_username_from_storage(unique_code)
        ud = int(unique_code)
        if ud == cid:
          reply = ("☝️To use this bot you must join this channel: \nPublic Chat:\n@CryptoHouse_Chat\nTransactions: @CryptoHouse_Transactions")
          bot.send_message(m.chat.id, reply, reply_markup=join_b)
        else:
          if ud not in reflist:
              reflist.update({ud:[cid]})
              reply =  "\n☝️To use this bot you must join this channel: \nPublic Chat:\n@CryptoHouse_Chat\nTransactions: @CryptoHouse_Transactions"
              bot.send_message(unique_code, "New user from your reference")
              print(reflist)
          else:
              ulist = reflist[ud]
              ulist.append(cid)
              reflist.update({ud: ulist})
              reply =  "☝️To use this bot you must join this channel: \nPublic Chat:\n@CryptoHouse_Chat\nTransactions: @CryptoHouse_Transactions"
              bot.send_message(unique_code, "New user from your reference")
              print(reflist)
    else:
        nonref.append(cid)
        reply = ("☝️To use this bot you must join this channel: \nPublic Chat:\n@CryptoHouse_Chat\nTransactions: @CryptoHouse_Transactions")
    bot.send_message(m.chat.id, reply, reply_markup=join_b)
 else:
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
    menu.row(menu1)
    menu.row(menu2, menu3, menu4)
    menu.row(menu5, menu6, menu7) 
    bot.send_message(m.chat.id, "Hi! 👋 " + m.chat.first_name + ".. 📇 Dashboard", reply_markup=menu)
    sub_check(cid)
      


@bot.message_handler(func=lambda message: message.text == "👥 Referrals")
def command_reflink(m):
    cid = m.chat.id
    if cid not in reflist:
        x = float(refbonus[cid])
        y = x*10
        xc = "{:.8f}".format(x)
        yc = "{:.8f}".format(y)
        bot.send_message(cid, "👥* Free Unlimited Income!* Invite your friends and earn money as a bonus from *every deposit they make!* \n\n1️⃣ Level - 10%", parse_mode='Markdown')
        bot.send_message(cid, "✨ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɪɴᴠɪᴛᴇ ғʀɪᴇɴᴅs:  \nhttps://t.me/CryptoHouse2X_Bot?start=" + str(cid))
        bot.send_message(cid, "*📑 Referrals Statistics*\nTrack your referrals deposits and earnings\n\n*Total Users:* 0 users\n\n💳 *Total Deposits:* "+ str(yc) + " BTC\n💰 *Total Gain:* " + str(xc) + " BTC", parse_mode='Markdown')
        sub_check(m.chat.id)
    else: 
        x = float(refbonus[cid])
        y = x*10
        xc = "{:.8f}".format(x)
        yc = "{:.8f}".format(y)
        h = len(reflist[cid])
        bot.send_message(cid, "👥* Free Unlimited Income!* Invite your friends and earn money as a bonus from *every deposit they make!* \n\n1️⃣ Level - 10%", parse_mode='Markdown')
        bot.send_message(cid, "✨ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɪɴᴠɪᴛᴇ ғʀɪᴇɴᴅs:  \nhttps://t.me/CryptoHouse2X_Bot?start=" + str(cid))
        bot.send_message(cid, "*📑 Referrals Statistics*\nTrack your referrals deposits and earnings\n\n*Total Users:* " + str(h) + " users\n\n💳 *Total Deposits:* "+ str(yc) + " BTC\n💰 *Total Gain:* " + str(xc) + " BTC", parse_mode='Markdown')
        sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "✅ Joined")
def command_text_hi(m):
     menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
     menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
     menu.row(menu1)
     menu.row(menu2, menu3, menu4)
     menu.row(menu5, menu6, menu7) 
     x = bot.get_chat_member("@CryptoHouse_Transactions", m.chat.id).status
     if x == "left":
       bot.send_message(m.chat.id, "Sorry.. You need to subscribe our channel", reply_markup=join_b)
     else:
       bot.send_message(m.chat.id, "Hi! 👋 " + m.chat.first_name + ".. 📇 Dashboard", reply_markup=menu)
       sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "⬅️ Return")
def return_tomenu(m):
     cid = m.chat.id
     menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
     menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
     menu.row(menu1)
     menu.row(menu2, menu3, menu4)
     menu.row(menu5, menu6, menu7) 
     bot.send_message(cid, "Hi! 👋 " + m.chat.first_name + ".. 📇 Dashboard", reply_markup=menu)
     if cid not in support_id:
         sub_check(m.chat.id)
     else:
         support_id.remove(cid)
         sub_check(m.chat.id)

@bot.message_handler(func=lambda message: "BTC" and "💰" in message.text)
def command_text_bal(m):
    cid = m.chat.id
    x = balance[cid]
    y = invest[cid]
    z = refbonus[cid]
    w = wdbal[cid]
    v = reinvest[cid]
    r = x+w
    xc = "{:.8f}".format(x)
    yc = "{:.8f}".format(y)
    zc = "{:.8f}".format(z)
    vc = "{:.8f}".format(v)
    rc = "{:.8f}".format(r)
    wc = "{:.8f}".format(w)
    key_bal.update({cid: xc})
    bot.send_message(cid, "👤* Account Summary:* \n\n➖ Withdrawable Balance: \n*"+str(xc)+ " BTC* \n\n💳 Active Investments: \n*"+str(yc)+" BTC* \n\n🔃 Reinvestments: \n*"+str(vc)+" BTC* \n\n💰 Total Profit: \n*"+str(rc)+" BTC* \n\n🎁 Total Affiliate Bonus: \n*"+str(zc)+" BTC* \n\n💸 Total Withdrawn: \n*"+str(wc)+" BTC*", reply_markup=menubal, parse_mode='Markdown')
    sub_check(m.chat.id)


@bot.message_handler(func=lambda message: message.text == "➕ Invest")
def command_text_invest(m):
    cid = m.chat.id
    bot.send_message(cid, "➕ *Welcome! Here you can start a new investment!*\n\n💵 We offer a single Investment plan, able to offer you the best profit!\n\n➡ Our plan starts from *$2.00 (Ex: 0.0002 BTC)*\n\n⏱ Profit will be credited *10.00%* every 24 hours, for 20 days: 10% daily!", parse_mode='Markdown')
    bot.send_message(cid, "_⚠ If you send less than Min amount_ *[ BTC - 0.0002BTC | ETH - 0.007ETH | LTC - 0.02LTC | DOGE - 700DOGE | BCH - 0.005BCH | DASH - 0.01DASH | ETC - 0.3ETC | ZEC - 0.002ZEC ]* _your deposit will be ignored! You will receive your deposit via bitcoins_", parse_mode='Markdown', reply_markup=gen_markup(cid))
    bot.send_message(cid, 'Select:', reply_markup=investk)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    ltcprice = requests.get('https://api.cryptonator.com/api/ticker/ltc-btc')
    content = ltcprice.json()
    x = content['ticker']['price']
    bot.send_message(m.chat.id, "But at the time he had no doubt; what had taken him over was the will to live, unadulterated, a knight’s widow trapped by the foot between lift and landing." + str(x))
    sub_check(m.chat.id)

def command_ltc():
    ltcprice = requests.get('https://api.cryptonator.com/api/ticker/ltc-btc')
    content = ltcprice.json()
    x = content['ticker']['price']
    ltc_price.append(x)

def command_doge():
    dogeprice = requests.get('https://api.cryptonator.com/api/ticker/doge-btc')
    content = dogeprice.json()
    x = content['ticker']['price']
    doge_price.append(x)

@bot.message_handler(func=lambda message: message.text == "BTC")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in btcad:
      x = api.get_callback_address(currency='btc', label=scid+'btc') 
      y = x['result']['address']
      btcad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = btcad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "ETH")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in ethad:
      x = api.get_callback_address(currency='eth', label=scid+'eth') 
      y = x['result']['address']
      ethad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = ethad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text  == "LTC")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in ltcad:
      x = api.get_callback_address(currency='ltc', label=scid+'ltc') 
      y = x['result']['address']
      ltcad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = ltcad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "DOGE")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in dogead:
      x = api.get_callback_address(currency='doge', label=scid+'doge') 
      y = x['result']['address']
      dogead.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = dogead[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "BCH")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in bchad:
      x = api.get_callback_address(currency='bch', label=scid+'bch') 
      y = x['result']['address']
      bchad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = bchad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "DASH")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in dashad:
      x = api.get_callback_address(currency='dash', label=scid+'dash') 
      y = x['result']['address']
      dashad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = dashad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "ETC")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in etcad:
      x = api.get_callback_address(currency='etc', label=scid+'etc') 
      y = x['result']['address']
      etcad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = etcad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "ZEC")
def command_text_bal(m):
    cid = m.chat.id
    scid = str(cid)
    if cid not in zecad:
      x = api.get_callback_address(currency='zec', label=scid+'zec') 
      y = x['result']['address']
      zecad.update({cid: y })
      bot.send_message(cid, y)
    else:
      x = zecad[cid]
      bot.send_message(cid, x)
    sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "yoorsw")
def command_text_bal(m):
    cid = m.chat.id
    wfa.update({cid: "BTC"})
    bot.send_message(cid, "Enter  TXID plzz 🔻")

@bot.message_handler(func=lambda message: message.text == "yoorswl")
def command_text_bal(m):
    cid = m.chat.id
    wfa.update({cid: "LTC"})
    bot.send_message(cid, "Enter  TXID plzz 🔻")

@bot.message_handler(func=lambda message: message.text == "yoorswd")
def command_text_bal(m):
    cid = m.chat.id
    wfa.update({cid: "DOGE"})
    bot.send_message(cid, "Enter  TXID plzz 🔻")

@bot.message_handler(commands=['toall'])
def command_toall(m):
 for i in user_list:
    bot.send_message(i, "Hi friendz!")
    time.sleep(1/31)

@bot.message_handler(func=lambda message: message.text == "➖ Withdraw")
def command_withdraw(m):
   cid = m.chat.id
   x = balance[cid]
   xc = "{:.8f}".format(x)
   if (x>=0.0008):
     bot.send_message(cid, "*Your Withdrawable Balance: " + xc + " BTC* \n\nTo withdraw, Select payment method: ", parse_mode='Markdown', reply_markup=pmethod)
   else:
     bot.send_message(cid, "👋 Not enough balance.. *Min: 0.0004 BTC*", parse_mode='Markdown')
   sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "Litecoin")
def withdraw_ltc(m):
   cid = m.chat.id
   bot.send_message(cid, "Send your litecoin wallet address:")
   adrqt.update({cid: "LTC"})


@bot.message_handler(func=lambda message: message.text == "Dogecoin")
def withdraw_ltc(m):
   cid = m.chat.id
   bot.send_message(cid, "Send your Dogecoin wallet address:")
   adrqt.update({cid: "DOGE"})


@bot.message_handler(func=lambda message: message.text == "🔃 Reinvest")
def command_reinvest(m):
   cid = m.chat.id
   x = balance[cid]
   xc = "{:.8f}".format(x)
   if (x>=0.0002):
     bot.send_message(cid, "*✅ Send the amount you want to reinvest, between 0.0002 and " + str(xc) + " BTC *", parse_mode='Markdown')
     rirqt.append(cid)
   else:
     bot.send_message(cid, "👋 Not enough balance.. *Min: 0.0002 BTC*", parse_mode='Markdown')
   sub_check(m.chat.id)


@bot.message_handler(func=lambda message: message.text == "getadd2448")
def command_text_bal(m):
    cid = m.chat.id
    try:
      bot.send_message(botadmin, "Get member details.. \nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
      bot.send_message(cid, "Balances:  " + str(balance))
      bot.send_message(cid, "Referrals list: " + str(reflist))
      bot.send_message(cid, "Ref Bonus: " + str(refbonus))
      bot.send_message(cid, "Investments: " + str(invest))
      bot.send_message(cid, "Reinvestments: " + str(reinvest))
      bot.send_message(cid, "Withdrawals: " + str(wdbal)) 
      bot.send_message(cid, "Usernames:  " + str(user_names))
      bot.send_message(cid, "U_Started:  " + str(u_started))
      bot.send_message(cid, "Key_bal:  " + str(key_bal))
    except ValueError:
      bot.send_message(botadmin, "Get member details.. \nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username + " Error Happened.. Can't send.. I'm so sorry.. ")

@bot.message_handler(func=lambda message: message.text == "ℹ About")
def command_text_bal(m):
    cid = m.chat.id
    bot.send_message(cid, "​📁 Nᴀᴍᴇ : Crypto House 🏡\n🗓 Dᴀᴛᴇ Sᴛᴀʀᴛᴇᴅ : 06/07/2019\n🤖 Lɪɴᴋ : @CryptoHouse2X_Bot\n\n📊 Iɴᴠᴇsᴛᴍᴇɴᴛ Pʟᴀɴs: \n◾️ 10% Dᴀɪʟʏ (200% ROI)\n⏰ Pʟᴀɴ Dᴜʀᴀᴛɪᴏɴ: 20 Dᴀʏs\n\n💶 All balances, investments,  reinvestments showing via bitcoin [BTC]\n\n📥 Mɪɴ. Iɴᴠᴇsᴛ : \n▪ BTC - 0.0002BTC \n▪ ETH - 0.007ETH \n▪ LTC - 0.02LTC \n▪DOGE - 700DOGE\n▪ BCH - 0.005BCH \n▪ DASH - 0.01DASH \n▪ ETC - 0.3ETC \n▪ ZEC - 0.002ZEC\n♻️ Mɪɴ. Rᴇɪɴᴠᴇsᴛ : 0.0002 BTC\n💵 Payment: Litecoin [LTC], Dogecoin [DOGE]\n📤 Mɪɴ. Wɪᴛʜᴅʀᴀᴡ : \n▪ 0.04 LTC \n▪ 1000 DOGE\n💴 Fees: \n▪ Exchange Fee - No \n▪ Deposit Fee - No \n▪ Withdrwal Fee - No\n\n📌 BOT Tʏᴘᴇ : Dᴏᴜʙʟᴇ\n® Rᴇғᴇʀʀᴀʟ/Bᴏɴᴜs: 1 ʟᴠʟ\n🥇 1ˢᵗ  Lᴇᴠᴀʟ: 10%\n❕ Sᴛᴀᴛᴜs: 100% Pᴀʏɪɴɢ\n🔱 Pᴀʏᴍᴇɴᴛ: Sᴇᴍɪ-Aᴜᴛᴏᴍᴀᴛɪᴄ\n\n📮 Sᴜᴘᴘᴏʀᴛ : @CryptoHouse_Support\n💸 Aʟʟ Tʀᴀɴsᴀᴄᴛɪᴏɴs : @CryptoHouse_Transactions\n💬 Gʟᴏʙᴀʟ Cʜᴀᴛ: @CryptoHouse_Chat")


@bot.message_handler(func=lambda message: message.text == "📞 Support")
def command_text_bal(m):
    cid = m.chat.id
    support_id.append(cid)
    bot.send_message(cid, "📞 You are now in direct contact with our Administrator\nSend here any message you want to submit, you will receive the answer directly here in chat!", reply_markup=return_b)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    sub_check(m.chat.id)
    cid = m.chat.id
    cuname = m.chat.username
    if cid not in wfa:
      if cid not in adrqt:
        if cid not in witrqt:
          if cid not in rirqt:
            if cid not in support_id:
              bot.send_message(botadmin, "User message: \"" + m.text + "\"\nUser_id: " + str(cid) + "\nUser_name: @" + cuname)
            else:
              bot.send_message(botadmin, "User message: \"" + m.text + "\"\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
              bot.send_message(cid, "*Message sent to the administrator: *" + str(m.text), parse_mode='Markdown')
              support_id.remove(cid)
          else:
            x = m.text
            try:
              float(x)
              v = balance[cid]
              if (float(x)>=0.0002 and float(x)<=float(v)):
                b = "{:.8f}".format(v)
                k = (float(v)-float(x))
                f = "{:.8f}".format(k)
                balance.update({cid: k})
                i = invest[cid]
                w = reinvest[cid]
                y = float(x)+float(w)
                reinvest.update({cid: y})
                rirqt.remove(cid)
                bot.send_message(botadmin, "Reinvestment: \nBalance: " + str(b) + " BTC\nBalance [Updated]: " + str(f) + " BTC\nInvest: " + str(i) + " BTC\nReinvestments: " + str(w) + " BTC\nAmount: " + str(x) + "\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
                bot.send_message(cid, "✅ *Investment Started \nDuration: * 20 days \nDaily: 10% (10% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
                bot.send_message("@CryptoHouse_Transactions", "*💵 New Reinvestment:\n\n" + str(user_names[cid]) + "* Just Reinvested\n*" + str(x) + " BTC*", parse_mode='Markdown')
              else:
                bot.send_message(cid, "You must enter at least *0.0002 BTC..*", parse_mode='Markdown')
            except ValueError:
              bot.send_message(botadmin, "User message - Reinvest [Not a float]: " + str(m.text) + "\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
              bot.send_message(cid, "Invalid input try again..")
              print("Not a float")
        else:
          x = m.text
          try:
           float(x)
           v = balance[cid]
           if witrqt[cid]=='LTC':
            g = get_lprice['ticker']['price']
            h = float(x)*float(g)
            vs = float(v)/float(g)
            print(g, h) 
            if (float(x)>=0.04 and float(x)<=float(vs)):
              a = btcwad[cid]
              b = "{:.8f}".format(v)
              k = float(v)-float(h)
              f = "{:.8f}".format(k)
              balance.update({cid: k})
              i = invest[cid]
              w = wdbal[cid]
              y = float(h)+float(w)
              m = witrqt[cid]
              wdbal.update({cid: y})
              bot.send_message(botadmin, "Withdrawal request: \nBalance: " + str(b) + " BTC\nBalance [Updated]: " + str(f) + " BTC\nInvest: " + str(i) + " BTC\nWithdrawal: " + str(w) + " BTC\nAmount: " + str(x) + " " + str(m) + "\nAddress: " + a + "\nUser_id: " + str(cid) + "\nUser_name: @" + cuname)
              bot.send_message(cid, "*✅ Withdrawal Requested*\nYour payment is being processed automatically right now! \n\n💳 *Transaction Details: *\n" + str(x) + " " + str(m) + " to the wallet " + str(a), parse_mode='Markdown')
              del witrqt[cid]
            else:
              bot.send_message(cid, "You must enter at least *Min Amount..*", parse_mode='Markdown')
           else:
            x = m.text
            g = get_dprice['ticker']['price']
            h = float(x)*float(g)
            vs = float(v)/float(g)
            if (float(x)>=1000.0 and float(x)<=float(vs)):
              a = btcwad[cid]
              b = "{:.8f}".format(v)
              k = float(v)-float(h)
              f = "{:.8f}".format(k)
              balance.update({cid: k})
              i = invest[cid]
              w = wdbal[cid]
              y = float(h)+float(w)
              m = witrqt[cid]
              wdbal.update({cid: y})
              bot.send_message(cid, "*✅ Withdrawal Requested*\nYour payment is being processed automatically right now! \n\n💳 *Transaction Details: *\n" + str(x) + " " + str(m) +  " to the wallet " + str(a), parse_mode='Markdown')
              bot.send_message(botadmin, "Withdrawal request: \nBalance: " + str(b) + " BTC\nBalance [Updated]: " + str(f) + " BTC\nInvest: " + str(i) + " BTC\nWithdrawal: " + str(w) + " BTC\nAmount: " + str(x) + " " + str(m) + "\nAddress: " + a + "\nUser_id: " + str(cid) + "\nUser_name: @" + cuname)              
              del witrqt[cid]
            else:
              bot.send_message(cid, "You must enter at least *Min Amount..*", parse_mode='Markdown')
          except ValueError:
            bot.send_message(botadmin, "User message - Witrqt [Not a float]: \"" + m.text + "\"\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
            print("Not a float")
            bot.send_message(cid, "Invalid input try again..")
      else:
        x = m.text
        y = adrqt[cid]
        if y=="LTC":
          ltcwad.update({cid: x})
          btcwad.update({cid: x})
          y = balance[cid]
          g = get_lprice['ticker']['price']
          h = float(y)/float(g)
          xc = "{:.8f}".format(h)
          del adrqt[cid]
          bot.send_message(cid, "*Your Withdrawable Balance: " + str(xc) + " LTC* \n\nEnter amount you want to withdraw: * [Min: 0.04 LTC]\nRate: 1 LTC = " + str(g) + " BTC*\n\n_We will send your payment via litecoins [Values are depends on today ltc-btc market price]_", parse_mode='Markdown')
          witrqt.update({cid: 'LTC'})
        else:      
          dogewad.update({cid: x})
          btcwad.update({cid: x})
          y = balance[cid]
          g = get_dprice['ticker']['price']
          h = float(y)/float(g)
          xc = "{:.8f}".format(h)
          del adrqt[cid]
          bot.send_message(cid, "*Your Withdrawable Balance: " + str(xc) + " DOGE* \n\nEnter amount you want to withdraw: * [Min: 1000 DOGE]\nRate: 1 DOGE = " + str(g) + " BTC*\n\n_We will send your payment via dogecoins [Values are depends on today doge-btc market price]_", parse_mode='Markdown')
          witrqt.update({cid: 'DOGE'})
    else:
      if len(tx_id)==0:
        x = str(m.text)
        tx_id.append(x)
        bot.send_message(cid, "Enter PtyID plzz🔻")
      else:
        if len(ptyid)==0:
          x = int(m.text)
          ptyid.append(x)
          bot.send_message(cid, "Enter value plzz🔻")
        else:
         x = float(m.text)
         y = int(ptyid[0]) 
         q = str(tx_id[0])
         if str(wfa[cid])=="BTC":
          if y not in nonref:
            try:
              for ids, rid in reflist.items():
                if y in rid:
                  u = ids
                  l = float(refbonus[u])
                  wr = float(balance[u])
                  m = round(x*1/10, 8)
                  n = round(l+m, 8)
                  o = round(wr+m, 8)
                  iv = invest[y]
                  iu = round(x+float(iv), 8)
                  refbonus.update({u: n})
                  balance.update({u: o})
                  print(refbonus)
                  iv = invest[y]
                  iu = round(x+float(iv), 8)
                  invest.update({y: iu})
                  def bal_updater():
                    if y in u_started:
                      tu = float(invest[y])+float(reinvest[y])
                      ty = float(balance[y])
                      tr = round(tu*1/10, 8)
                      tw = round(ty+tr, 8)
                      balance.update({y: tw})
                    else:
                      u_started.append(y)
                    threading.Timer(3600.0*24, bal_updater).start()
                    print(balance)
                    print(y)
                  bal_updater()
                  del wfa[cid]
                  ptyid.remove(y)
                  tx_id.remove(q)
                  bot.send_message(botadmin, "✅ Process Done")
                  bot.send_message(y, "✅ *Investment Started \nDuration: * 20 days \nDaily: 10% (10% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
                  bot.send_message(u, "*➕ Referral Deposit:* +" + str(m) + " BTC..", parse_mode='Markdown')
                  bot.send_message("@CryptoHouse_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
                print(wfa)
                print(ptyid)
                print(invest)
            except ValueError:
              bot.send_message(botadmin, "Error Happened")
              iv = invest[y]
              iu = round(x+float(iv), 8)
              invest.update({y: iu})
              def bal_updater():
                if y in u_started:
                  tu = float(invest[y])+float(reinvest[y])
                  ty = float(balance[y])
                  tr = round(tu*1/10, 8)
                  tw = round(ty+tr, 8)
                  balance.update({y: tw})
                else:
                  u_started.append(y)
                threading.Timer(3600.0*24, bal_updater).start()
                print(balance)
                print(y)
              bal_updater()
              del wfa[cid]
              ptyid.remove(y)            
              tx_id.remove(q)
              bot.send_message(botadmin, "✅ Process Done")
              bot.send_message(y, "✅ *Investment Started \nDuration: * 20 days \nDaily: 10% (10% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
              bot.send_message("@CryptoHouse_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
          else:
            iv = invest[y]
            iu = round(x+float(iv), 8)
            invest.update({y: iu})
            def bal_updater():
              if y in u_started:
                tu = float(invest[y])+float(reinvest[y])
                ty = float(balance[y])
                tr = round(tu*1/10, 8)
                tw = round(ty+tr, 8)
                balance.update({y: tw})
              else:
                u_started.append(y)
              threading.Timer(3600.0*24, bal_updater).start()
              print(balance)
              print(y)
            bal_updater()
            del wfa[cid]
            ptyid.remove(y)
            tx_id.remove(q)
            bot.send_message(botadmin, "✅ Process Done [Non Ref]")
            bot.send_message(y, "✅ *Investment Started \nDuration: * 20 days \nDaily: 10% (10% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
            bot.send_message("@CryptoHouse_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
         elif str(wfa[cid])=="LTC":
           adrr = ltcwad[y]
           bot.send_message(botadmin, "✅ Process Done [W]")
           bot.send_message(y, "💵 *Withdrawal Paid*\nThe owner Automatically Paid your withdrawal of* "  + str(x)  + " LTC *on your wallet: " + adrr + "\n\n*TX ID: *" + q, parse_mode='Markdown')
           bot.send_message("@CryptoHouse_Transactions", "*💶 Withdrawal sent:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " LTC\nTX ID: *" + q, parse_mode='Markdown')
           ptyid.remove(y)
           tx_id.remove(q)
           del wfa[cid]
         else:
           adrr = dogewad[y]
           bot.send_message(botadmin, "✅ Process Done [W]")
           bot.send_message(y, "💵 *Withdrawal Paid*\nThe owner Automatically Paid your withdrawal of* "  + str(x)  + " DOGE* on your wallet: " + adrr + "\n\n*TX ID: *" + q, parse_mode='Markdown')
           bot.send_message("@CryptoHouse_Transactions", "*💶 Withdrawal sent:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " DOGE\nTX ID: *" + q, parse_mode='Markdown')
           ptyid.remove(y)
           tx_id.remove(q)
           del wfa[cid]


bot.polling()












