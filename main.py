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

get_lprice = ltcprice.json()
print("Name:", get_lprice['ticker']['price'])
get_dprice = dogeprice.json()

api = CoinPaymentsAPI(public_key='a0d8eb09688f0b074d2cfa89832b58535fdf5fc82d47bae90b5304c080c0e29c', private_key='77b1dc1711A5E077e1cbdCE5629353838849D9a2D549Cc6286b188525f256170')

bot = telebot.TeleBot('830970184:AAFcyf4LQfTe8lKTqTO2VHIYwyaedfwVTP4')

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
ltcad = {}
dogead = {}
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
pibal = {}
prbal = {}
ur_started = []


def sub_check(c_id):
     i = int(c_id)
     x = bot.get_chat_member("@CrowdBtc_Transactions", i).status
     if x == "left":
       bot.send_message(i, "Sorry.. You need to subscribe our channel: \nPublic Chat:\n@CrowdBtc_Chat\nTransactions: @CrowdBtc_Transactions", reply_markup=join_b)
     else:
       print(time.time())


def gen_markup(ccid):
    markup = InlineKeyboardMarkup()
    markup.row_width = 8
    markup.add(InlineKeyboardButton("Check Exchange Rates", callback_data=ccid))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  try:
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
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [callback]")


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
  try:
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [user_step]")

def listener(messages):
  try:
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Listner]")

bot.set_update_listener(listener) 

def extract_unique_code(text):
  try:
    return text.split()[1] if len(text.split()) > 1 else None
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Unq_code]")

def in_storage(unique_code):
    return True

def get_username_from_storage(unique_code):
  try:
    return "ABC" if in_storage(unique_code) else None
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [unq2]")

def save_chat_id(chat_id, username):
    pass



@bot.message_handler(commands=['start']) 
def send_welcome(m):
  try:
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
           reply = ("☝️To use this bot you must join this channel: \nPublic Chat:\n@CrowdBtc_Chat\nTransactions:\n @CrowdBtc_Transactions")
           bot.send_message(m.chat.id, reply, reply_markup=join_b)
         else:
           if ud not in reflist:
               reflist.update({ud:[cid]})
               reply =  "\n☝️To use this bot you must join this channel: \nPublic Chat:\n@CrowdBtc_Chat\nTransactions:\n @CrowdBtc_Transactions"
               bot.send_message(m.chat.id, reply, reply_markup=join_b)
               try:
                  bot.send_message(unique_code, "New user from your reference")
               except:
                  bot.send_message(botadmin, "Chat not found" + unique_code)
           else:
               ulist = reflist[ud]
               ulist.append(cid)
               reflist.update({ud: ulist})
               reply =  "☝️To use this bot you must join this channel: \nPublic Chat:\n@CrowdBtc_Chat\nTransactions:\n @CrowdBtc_Transactions"
               bot.send_message(m.chat.id, reply, reply_markup=join_b)
               try:
                  bot.send_message(unique_code, "New user from your reference")
               except:
                  bot.send_message(botadmin, "Chat not found" + unique_code)
      else:
         nonref.append(cid)
         reply = ("☝️To use this bot you must join this channel: \nPublic Chat:\n@CrowdBtc_Chat\nTransactions:\n @CrowdBtc_Transactions")
         bot.send_message(m.chat.id, reply, reply_markup=join_b)
    else:
       menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
       menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
       menu.row(menu1)
       menu.row(menu2, menu3, menu4)
       menu.row(menu5, menu6, menu7) 
       bot.send_message(m.chat.id, "📇 Dashboard\nHi! 👋 " + m.chat.first_name + "..", reply_markup=menu)
       sub_check(cid)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [start]")
     bot.send_message(m.chat.id, "Restart bot here 👉 /start")




@bot.message_handler(func=lambda message: message.text == "👥 Referrals")
def command_reflink(m):
  try:
     cid = m.chat.id
     if cid not in reflist:
         x = float(refbonus[cid])
         y = x*10
         xc = "{:.8f}".format(x)
         yc = "{:.8f}".format(y)
         bot.send_message(cid, "👥* Free Unlimited Income!* Invite your friends and earn money as a bonus from *every deposit they make!* \n\n1️⃣ Level - 10%", parse_mode='Markdown')
         bot.send_message(cid, "✨ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɪɴᴠɪᴛᴇ ғʀɪᴇɴᴅs:  \nhttps://t.me/CrowdBtc_Bot?start=" + str(cid))
         bot.send_message(cid, "*📑 Referrals Statistics*\nTrack your referrals deposits and earnings\n\n*Total Users:* 0 users\n\n💳 *Total Deposits:* "+ str(yc) + " BTC\n💰 *Total Gain:* " + str(xc) + " BTC", parse_mode='Markdown')
         sub_check(m.chat.id)
     else: 
         x = float(refbonus[cid])
         y = x*10
         xc = "{:.8f}".format(x)
         yc = "{:.8f}".format(y)
         h = len(reflist[cid])
         bot.send_message(cid, "👥* Free Unlimited Income!* Invite your friends and earn money as a bonus from *every deposit they make!* \n\n1️⃣ Level - 10%", parse_mode='Markdown')
         bot.send_message(cid, "✨ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɪɴᴠɪᴛᴇ ғʀɪᴇɴᴅs:  \nhttps://t.me/CrowdBtc_Bot?start=" + str(cid))
         bot.send_message(cid, "*📑 Referrals Statistics*\nTrack your referrals deposits and earnings\n\n*Total Users:* " + str(h) + " users\n\n💳 *Total Deposits:* "+ str(yc) + " BTC\n💰 *Total Gain:* " + str(xc) + " BTC", parse_mode='Markdown')
         sub_check(m.chat.id)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Referral]")

@bot.message_handler(func=lambda message: message.text == "✅ Joined")
def command_text_hi(m):
  try:
      menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
      menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
      menu.row(menu1)
      menu.row(menu2, menu3, menu4)
      menu.row(menu5, menu6, menu7) 
      x = bot.get_chat_member("@CrowdBtc_Transactions", m.chat.id).status
      if x == "left":
        bot.send_message(m.chat.id, "Sorry.. You need to subscribe our channel", reply_markup=join_b)
      else:
        bot.send_message(m.chat.id, "📇 Dashboard\nHi! 👋 " + m.chat.first_name + "..", reply_markup=menu)
        sub_check(m.chat.id)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Join]")
     bot.send_message(m.chat.id, "Restart bot here 👉 /start")

@bot.message_handler(func=lambda message: message.text == "⬅️ Return")
def return_tomenu(m):
  try:
      cid = m.chat.id
      menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
      menu1 = types.KeyboardButton('💰 ' + str(key_bal[m.chat.id]) + ' BTC')
      menu.row(menu1)
      menu.row(menu2, menu3, menu4)
      menu.row(menu5, menu6, menu7) 
      bot.send_message(cid, "📇 Dashboard\nHi! 👋 " + m.chat.first_name + "..", reply_markup=menu)
      if cid not in support_id:
          sub_check(m.chat.id)
      else:
          support_id.remove(cid)
      if cid not in adrqt:
          sub_check(m.chat.id)
      else:
          del adrqt[cid]
      if cid not in witrqt:
          sub_check(m.chat.id)
      else:
          del witrqt[cid]
      if cid not in rirqt:
          sub_check(m.chat.id)
      else:
          rirqt.remove(cid)
      sub_check(m.chat.id)
      try:
          x = balance[cid]
          xc = "{:.8f}".format(x)
          key_bal.update({cid: xc})
      except:
          bot.send_message(botadmin, "Error man.. WTF 😠 [Return Bal]")
          bot.send_message(m.chat.id, "Restart bot here 👉 /start")
  except:
      bot.send_message(botadmin, "Error man.. WTF 😠 [Return]")
      bot.send_message(m.chat.id, "Restart bot here 👉 /start")

  
try:
 @bot.message_handler(func=lambda message: "💰" in message.text and "BTC" in message.text)
 def command_text_bal(m):
  try:
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
  except:
     bot.send_message(botadmin, "Key error man.. WTF 😠")
     bot.send_message(m.chat.id, "Restart bot here 👉 /start")
except:
 bot.send_message(botadmin, "Error Man WTF (Bal)")
 bot.send_message(m.chat.id, "Restart bot here 👉 /start")

@bot.message_handler(func=lambda message: message.text == "➕ Invest")
def command_text_invest(m):
  try:
     cid = m.chat.id
     bot.send_message(cid, "➕ *Welcome! Here you can start a new investment!*\n\n💵 We offer a single Investment plan, able to offer you the best profit!\n\n➡ Our plan starts from *$2.00 (Ex: 0.0002 BTC)*\n\n⏱ Profit will be credited *50.00%* every 24 hours, for 4 days: 50% daily!", parse_mode='Markdown')
     bot.send_message(cid, "_⚠ If you send less than Min amount your deposit will be ignored! You will receive your deposit via bitcoins_", parse_mode='Markdown')
     try:
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
     except:
       bot.send_message(botadmin, "Error man.. WTF 😠 [BTC]")
       bot.send_message(cid, 'Select:', reply_markup=return_b)
     sub_check(m.chat.id)
  except:
     bot.send_message(botadmin, "Invest error man.. WTF 😠")



@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
     ltcprice = requests.get('https://api.cryptonator.com/api/ticker/ltc-btc')
     content = ltcprice.json()
     x = content['ticker']['price']
     bot.send_message(m.chat.id, "But at the time he had no doubt; what had taken him over was the will to live, unadulterated, a knight’s widow trapped by the foot between lift and landing." + str(x))
     sub_check(m.chat.id)

@bot.message_handler(func=lambda message: message.text == "yoorsw")
def command_text_bal(m):
     cid = m.chat.id
     wfa.update({cid: "BTC"})
     bot.send_message(cid, "Enter  TXID plzz 🔻")
 
@bot.message_handler(func=lambda message: message.text == "yoorswb")
def command_text_bal(m):
     cid = m.chat.id 
     wfa.update({cid: "btc"})
     bot.send_message(cid, "Enter  TXID plzz 🔻")


@bot.message_handler(commands=['toall'])
def command_toall(m):
  for i in user_list:
     bot.send_message(i, "Hi friendz!")
     time.sleep(1/31)

@bot.message_handler(func=lambda message: message.text == "➖ Withdraw")
def command_withdraw(m):
  try:
    cid = m.chat.id
    x = balance[cid]
    xc = "{:.8f}".format(x)
    if (x>=0.0004):
      bot.send_message(cid, "*Your Withdrawable Balance: " + xc + " BTC* \n\nTo withdraw, Select payment method: ", parse_mode='Markdown')
      bot.send_message(cid, "Send your Bitcoin wallet address:", reply_markup=return_b)
      adrqt.update({cid: "BTC"})
    else:
      bot.send_message(cid, "👋 Not enough balance.. *Min: 0.0004 BTC*", parse_mode='Markdown')
    sub_check(m.chat.id)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Withdraw]")


@bot.message_handler(func=lambda message: message.text == "🔃 Reinvest")
def command_reinvest(m):
  try:
    cid = m.chat.id
    x = balance[cid]
    xc = "{:.8f}".format(x)
    if (x>=0.0002):
      bot.send_message(cid, "*✅ Send the amount you want to reinvest, between 0.0002 and " + str(xc) + " BTC *", parse_mode='Markdown', reply_markup=return_b)
      rirqt.append(cid)
    else:
      bot.send_message(cid, "👋 Not enough balance.. *Min: 0.0002 BTC*", parse_mode='Markdown')
    sub_check(m.chat.id)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Reinvest]")

@bot.message_handler(commands=['toallll'])
def command_toallll(m):
  try:
   for i in user_list:
     x = m.text
     s = x.replace('/toallll', '')
     bot.send_message(i, s)
     time.sleep(1/31)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [toallll]")
    
@bot.message_handler(commands=['admsg'])
def command_admsg(m):
  try:
     x = m.text
     u = x.replace('/admsg', '')
     splitted = u.split()
     cid = splitted[0]
     s = u.replace(cid, '')
     bot.send_message(cid, s)    
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [admsg]")
   
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
     except:
       bot.send_message(botadmin, "Get member details.. \nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username + " Error Happened.. Can't send.. I'm so sorry.. ")

@bot.message_handler(func=lambda message: message.text == "ckadmin")
def command_adminc(m):
   ptyid.remove(y)
   tx_id.remove(q)
   del wfa[cid]
     
@bot.message_handler(func=lambda message: message.text == "ℹ About")
def command_text_bal(m):
  try:
     cid = m.chat.id
     bot.send_message(cid, "​📁 Nᴀᴍᴇ : Crowd BTC\n🗓 Dᴀᴛᴇ Sᴛᴀʀᴛᴇᴅ : 07/07/2019\n🤖 Lɪɴᴋ : @CrowdBtc_Bot\n\n📊 Iɴᴠᴇsᴛᴍᴇɴᴛ Pʟᴀɴs: \n◾️ 50% Dᴀɪʟʏ (200% ROI)\n⏰ Pʟᴀɴ Dᴜʀᴀᴛɪᴏɴ: 4 Dᴀʏs\n\n📥 Mɪɴ. Iɴᴠᴇsᴛ : \n▪ BTC - 0.0002BTC \n♻️ Mɪɴ. Rᴇɪɴᴠᴇsᴛ : 0.0002 BTC\n📤 Mɪɴ. Wɪᴛʜᴅʀᴀᴡ : \n▪ 0.0004 BTC\n💴 Fees: \n▪ Deposit Fee - No \n▪ Withdrwal Fee - No\n\n📌 BOT Tʏᴘᴇ : Dᴏᴜʙʟᴇ\n® Rᴇғᴇʀʀᴀʟ/Bᴏɴᴜs: 1 ʟᴠʟ\n🥇 1ˢᵗ  Lᴇᴠᴀʟ: 10%\n❕ Sᴛᴀᴛᴜs: 100% Pᴀʏɪɴɢ\n🔱 Pᴀʏᴍᴇɴᴛ: Sᴇᴍɪ-Aᴜᴛᴏᴍᴀᴛɪᴄ\n\n📮 Sᴜᴘᴘᴏʀᴛ : @CrowdBtc_Support\n💸 Aʟʟ Tʀᴀɴsᴀᴄᴛɪᴏɴs : @CrowdBtc_Transactions\n💬 Gʟᴏʙᴀʟ Cʜᴀᴛ: @CrowdBtc_Chat")
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [About]")

@bot.message_handler(func=lambda message: message.text == "📞 Support")
def command_text_bal(m):
  try:
     cid = m.chat.id
     support_id.append(cid)
     bot.send_message(cid, "📞 You are now in direct contact with our Administrator\nSend here any message you want to submit, you will receive the answer directly here in chat!", reply_markup=return_b)
  except:
     bot.send_message(botadmin, "Error man.. WTF 😠 [Support]")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
  try:
     sub_check(m.chat.id)
     cid = m.chat.id
     cuname = m.chat.username
     if cid not in wfa:
       if cid not in adrqt:
         if cid not in witrqt:
           if cid not in rirqt:
             if cid not in support_id:
               bot.send_message(botadmin, "User message: " + str(m.text) + " \nUser_id: " + str(cid) + "\nUser_name: @" + cuname)
             else:
               bot.send_message(botadmin, "User message[Sup]: " + str(m.text) + " \nUser_id: " + str(cid) + "\nUser_name: @" + cuname)
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
                 yy = float(x)+float(w)
                 reinvest.update({cid: yy})
                 rirqt.remove(cid)
                 y = m.chat.id
                 def rebal_updater():
                   if y in ur_started:
                     tcc = float(reinvest[y])*2
                     gg = float(prbal[y])
                     if (float(tcc)>float(gg)):
                       tu = float(reinvest[y])
                       ty = float(balance[y])
                       tii = float(prbal[y])
                       tr = round(tu*1/2, 8)
                       tw = round(ty+tr, 8)
                       ta = float(tii+tr)
                       balance.update({y: tw})                    
                       prbal.update({y: ta})
                       threading.Timer(3600.0*24, rebal_updater).start()
                     else:
                       prbal.update({y: 0})
                       reinvest.update({y: 0})
                       ur_started.remove(y)
                       threading.Timer(3600.0*24, rebal_updater).cancel()
                   else:
                     ur_started.append(y)
                     prbal.update({y: 0})
                     threading.Timer(3600.0*24, rebal_updater).start()
                 rebal_updater()
                 bot.send_message(botadmin, "Reinvestment: \nBalance: " + str(b) + " BTC\nBalance [Updated]: " + str(f) + " BTC\nInvest: " + str(i) + " BTC\nReinvestments: " + str(w) + " BTC\nAmount: " + str(x) + "\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
                 bot.send_message(cid, "✅ *Investment Started \nDuration: * 4 days \nDaily: 50% (50% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
                 bot.send_message("@CrowdBtc_Transactions", "*💵 New Reinvestment:\n\n" + str(user_names[cid]) + "* Just Reinvested\n*" + str(x) + " BTC*", parse_mode='Markdown')
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
             if (float(x)>=0.0004 and float(x)<=float(v)):
               a = btcwad[cid]
               b = "{:.8f}".format(v)
               k = float(v)-float(x)
               f = "{:.8f}".format(k)
               balance.update({cid: k})
               i = invest[cid]
               w = wdbal[cid]
               y = float(x)+float(w)
               m = witrqt[cid]
               wdbal.update({cid: y})
               bot.send_message(botadmin, "Withdrawal request: \nBalance: " + str(b) + " BTC\nBalance [Updated]: " + str(f) + " BTC\nInvest: " + str(i) + " BTC\nWithdrawal: " + str(w) + " BTC\nAmount: " + str(x) + " " + str(m) + "\nAddress: " + a + "\nUser_id: " + str(cid) + "\nUser_name: @" + cuname)
               bot.send_message(cid, "*✅ Withdrawal Requested*\nYour payment is being processed automatically right now! \n\n💳 *Transaction Details: *\n" + str(x) + " " + str(m) + " to the wallet " + str(a), parse_mode='Markdown')
               del witrqt[cid]
             else:
               bot.send_message(cid, "You must enter at least *Min Amount..*", parse_mode='Markdown')
           except ValueError:
               bot.send_message(botadmin, "User message - Witrqt [Not a float]: \"" + m.text + "\"\nUser_id: " + str(cid) + "\nUser_name: @" + m.chat.username)
               print("Not a float")
               bot.send_message(cid, "Invalid input try again..")
       else:
           x = str(m.text)
           btcwad.update({cid: x})
           y = balance[cid]
           xc = "{:.8f}".format(y)
           del adrqt[cid]
           bot.send_message(cid, "*Your Withdrawable Balance: " + str(xc) + " BTC* \n\nEnter amount you want to withdraw: * [Min: 0.0004 BTC]*", parse_mode='Markdown')
           witrqt.update({cid: 'BTC'})
     else:
      try:
       if len(tx_id)==0:
         x = str(m.text)
         tx_id.append(x)
         bot.send_message(cid, "Enter PtyID plzz🔻")
      except:
         bot.send_message(botadmin, "Error")
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
                       tcc = float(invest[y])*2
                       gg = float(pibal[y])
                       if (float(tcc)>float(gg)):
                         tu = float(invest[y])
                         ty = float(balance[y])
                         tii = float(pibal[y])
                         tr = round(tu*1/2, 8)
                         tw = round(ty+tr, 8)
                         ta = float(tii+tr)
                         balance.update({y: tw})                    
                         pibal.update({y: ta})
                         threading.Timer(3600.0*24, bal_updater).start()
                       else:
                         pibal.update({y: 0})
                         invest.update({y: 0})
                         u_started.remove(y)
                         threading.Timer(3600.0*24, bal_updater).cancel()
                     else:
                       u_started.append(y)
                       pibal.update({y: 0})
                       threading.Timer(3600.0*24, bal_updater).start()
                   bal_updater()
                   del wfa[cid]
                   ptyid.remove(y)
                   tx_id.remove(q)
                   bot.send_message(botadmin, "✅ Process Done")
                   bot.send_message(y, "✅ *Investment Started \nDuration: * 4 days \nDaily: 50% (50% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
                   bot.send_message("@CrowdBtc_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
                   try:
                     bot.send_message(u, "*➕ Referral Deposit:* +" + str(m) + " BTC..", parse_mode='Markdown')
                   except:
                     bot.send_message(botadmin, "Chat not found" + u)
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
                   tcc = float(invest[y])*2
                   gg = float(pibal[y])
                   if (float(tcc)>float(gg)):
                     tu = float(invest[y])
                     ty = float(balance[y])
                     tii = float(pibal[y])
                     tr = round(tu*1/2, 8)
                     tw = round(ty+tr, 8)
                     ta = float(tii+tr)
                     balance.update({y: tw})                    
                     pibal.update({y: ta})
                     threading.Timer(3600.0*24, bal_updater).start()
                   else:
                     pibal.update({y: 0})
                     invest.update({y: 0})
                     u_started.remove(y)
                     threading.Timer(3600.0*24, bal_updater).cancel()
                 else:
                   u_started.append(y)
                   pibal.update({y: 0})
                   threading.Timer(3600.0*24, bal_updater).start()
               bal_updater()
               del wfa[cid]
               ptyid.remove(y)            
               tx_id.remove(q)
               bot.send_message(botadmin, "✅ Process Done")
               bot.send_message(y, "✅ *Investment Started \nDuration: * 4 days \nDaily: 50% (50% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
               bot.send_message("@CrowdBtc_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
           else:
             iv = invest[y]
             iu = round(x+float(iv), 8)
             invest.update({y: iu})
             def bal_updater():
               if y in u_started:
                 tcc = float(invest[y])*2
                 gg = float(pibal[y])
                 if (float(tcc)>float(gg)):
                   tu = float(invest[y])
                   ty = float(balance[y])
                   tii = float(pibal[y])
                   tr = round(tu*1/2, 8)
                   tw = round(ty+tr, 8)
                   ta = float(tii+tr)
                   balance.update({y: tw})                    
                   pibal.update({y: ta})
                   threading.Timer(3600.0*24, bal_updater).start()
                 else:
                   pibal.update({y: 0})
                   invest.update({y: 0})
                   u_started.remove(y)
                   threading.Timer(3600.0*24, bal_updater).cancel()
               else:
                 u_started.append(y)
                 pibal.update({y: 0})
                 threading.Timer(3600.0*24, bal_updater).start()
             bal_updater()
             del wfa[cid]
             ptyid.remove(y)
             tx_id.remove(q)
             bot.send_message(botadmin, "✅ Process Done [Non Ref]")
             bot.send_message(y, "✅ *Investment Started \nDuration: * 4 days \nDaily: 50% (50% every 24 hours) \nAmount: " + str(x) + " BTC", parse_mode='Markdown')
             bot.send_message("@CrowdBtc_Transactions", "*💵 New Investment:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
          else:
            adrr = btcwad[y]
            bot.send_message(botadmin, "✅ Process Done [W]")
            bot.send_message(y, "💵 *Withdrawal Paid*\nThe owner Automatically Paid your withdrawal of* "  + str(x)  + " BTC* on your wallet: " + adrr + "\n\n*TX ID: *" + q, parse_mode='Markdown')
            bot.send_message("@CrowdBtc_Transactions", "*💶 Withdrawal sent:\n\n" + str(user_names[y]) + "* Just Invested\n*" + str(x) + " BTC\nTX ID: *" + q, parse_mode='Markdown')
            ptyid.remove(y)
            tx_id.remove(q)
            del wfa[cid]
  except:
     bot.send_message(m.chat.id, "Something went wrong.. Plzz try again.. Click here to restart 👉 /start")
     bot.send_message(botadmin, "Something went wrong.. WTF 😠 [Text]")



bot.polling()








