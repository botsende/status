import vk_api

import datetime # работа с датой и временем

import time
while True:
  vk = vk_api.VkApi(token="ccb184b9b89bf4ed56eccd11f061c0d2cfcc61d6a3c773d4ea6d7e3f69d419ce319977f7e48ddedecd375")
  delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
  t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
  nowtime = t.strftime("%H:%M") # текущее время
  nowdate = t.strftime("%d.%m.%Y") # текущая дата
  on = vk.method("friends.getOnline") # получаем список id друзей онлайн
  counted = len(on) # считаем кол-во элементов в списке
  vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})
  time.sleep(30) # погружаем скрипт в «сон» на 30 секунд