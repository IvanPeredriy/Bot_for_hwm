from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import random

last_stavka = 0
flag_win = False
buf_money_earned = 0
first_start = 1
ext = 0
n = [1000,1000,2000,3000,5000,8000,13000,21000]      


class bot():
    last_stavka = 0
    def __init__ (self, login, password, site):
        self.login = login
        self.password = password
        self.site = site
        self.browser = webdriver.Firefox()
        pass

    def log (self):
        self.browser.get(self.site)
        element = self.browser.find_element_by_name("login")
        element.clear()
        element.send_keys(self.login)
        element = self.browser.find_element_by_name("pass")
        element.clear()
        element.send_keys(self.password)
        element.click()
        element = self.browser.find_element_by_class_name('entergame')
        element.click()
        element = self.browser.find_element_by_css_selector('#top_res_table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)').text
        money_today = element
        print("Добро пожаловать в игру! Текущее состояние: {0} золотых".format(element))
        pass
    
    def ruletka(self):
        element = self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[4]/table/tbody/tr/td[9]/table/tbody/tr[2]/td/table/tbody/tr/td/div/ul/li/nobr/a/b')
        element.click()
        def fibonacci(self):                # Ставка в рулетку подкорректированной системой Фибоначчи. 1 1 2 3 5 8 13
            global last_stavka
            global first_start
            global stavka
            global n
            if first_start == 1:
                first_start=0
                last_stavka=0
                stavka=1000
                return stavka
            if flag_win == True:
                stavka = 1000
                last_stavka = 0
                first_start = 0
                return stavka
            else:
                stavka = n[last_stavka]
                last_stavka = last_stavka + 1
                return stavka
            pass
        element = self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[4]/table/tbody/tr/td[9]/table/tbody/tr[2]/td/table/tbody/tr/td/div/ul/li/nobr/a/b')
        element.click()
        element = self.browser.find_element_by_css_selector('td.txt > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(6) > a:nth-child(4)')
        element.click()
        try:
            #element = self.browser.find_element_by_css_selector('table.wbwhite > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(3)')
            element = self.browser.find_element_by_css_selector('table.wbwhite > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(3) > font:nth-child(1) > b:nth-child(1)')
            #element.isDisplayed()
        except AttributeError:
            print(Exception)
            flag_win = True
        else:
            element = self.browser.find_element_by_css_selector('table.wbwhite > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(3) > font:nth-child(1) > b:nth-child(1)').text
            #if element != 'RED':
            if element == '1':
                flag_win = True
                pass
            elif element == '3':
                flag_win = True
                pass
            elif element == '5':
                flag_win = True
                pass
            elif element == '7':
                flag_win = True
                pass
            elif element == '9':
                flag_win = True
                pass
            elif element == '12':
                flag_win = True
                pass
            elif element == '14':
                flag_win = True
                pass
            elif element == '16':
                flag_win = True
                pass
            elif element == '18':
                flag_win = True
                pass
            elif element == '19':
                flag_win = True
                pass
            elif element == '21':
                flag_win = True
                pass
            elif element == '23':
                flag_win = True
                pass
            elif element == '25':
                flag_win = True
                pass
            elif element == '27':
                flag_win = True
                pass
            elif element == '30':
                flag_win = True
                pass
            elif element == '32':
                flag_win = True
                pass
            elif element == '34':
                flag_win = True
                pass
            elif element == '36':
                flag_win = True
                pass
            else:
                flag_win = False
                pass

        self.browser.back()
        # Тут ставит красное поле
        element = self.browser.find_element_by_css_selector('table.wb:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(3) > div:nth-child(1) > img:nth-child(1)')
        element.click()
        element = self.browser.find_element_by_name("bet")
        element.clear()
        element.click()
        element.send_keys(fibonacci(self))
        element = self.browser.find_element_by_css_selector('table.wb:nth-child(4) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)')
        element.click()
        pass

last_stavka = 0
flag_win = False
nick = bot(login = "", password = "", site = "http://www.heroeswm.ru/")
nick.log()

while True:
    
    nick.ruletka()
    time_of_sleep = 300+random.randint(-60, 60)
    d = datetime.datetime.now()
    if flag_win == True:
        Otchet = '\n\n\nСтавка выиграла!\n'
    else:
        Otchet = '\n\n\nСтавка проиграла!\n'
    print(' {0} \n Дело сделано! Поставил {1} золотых! Буду спать {2} секунд'.format(d, stavka ,time_of_sleep))
    time.sleep(time_of_sleep)
    if ext == 1:                                                        # Тут как-то запилить, чтобы можно было каждые 10 минут давать n времени на остановку программы. Тогда можно было бы прикрутить и вывод "Сегодня заработано столько-то". По крайней мере код потихоньку к этому готовлю (Иван, money_today и текущее состояние {0} золотых)
        print('''Текущее состояние:
        За сегодня заработано: ''')
        raise SystemExit(1)

