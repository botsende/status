import vk_api

import datetime # работа с датой и временем

import time
while True:
  vk = vk_api.VkApi(token="ccb184b9b89bf4ed56eccd11f061c0d2cfcc61d6a3c773d4ea6d7e3f69d419ce319977f7e48ddedecd375")
  time1=0
  while(1):
    delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
    nowdate = t.strftime("%d.%m") # текущая дата
    print("yes")
    time.sleep(5)
    if nowdate == "01.01":
      print(nowdate)
      while(1):
          time1 = time1 + 1
          vk.method("status.set", {"text": f"{time1} минут, прошло с нового года🧣🎄🤞"})
          time.sleep(60) # погружаем скрипт в «сон» на 30 секунд
        