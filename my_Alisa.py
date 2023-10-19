import speech_recognition as sr
import pygame
from gtts import gTTS
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup
from math import *

def record1():
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(n)
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()

def enter():
    record = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Скажите что-нибудь...')
        audio = record.listen(source)
        speech = record.recognize_google(audio, language='ru_RU').lower()
        print(speech)

record = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print('Скажите что-нибудь...')
    audio = record.listen(source)
    speech = record.recognize_google(audio, language='ru_RU').lower()
    print(speech)


# if speech == 'привет':
#     print('Добрый день')

# if speech == 'какое сегодня число':
#     print('Сегодня 30 июля')

if speech == 'привет' or speech == 'добрый день':
    # answers = ['добрый день', 'здравствуйте']
    # n = random.choice(answers)
    n = 'добрый день'
    record1()
elif speech == 'сколько время' or speech == 'сколько сейчас времени' or speech == 'сколько сейчас время' or speech == 'сколько времени':
    # time1 = datetime.now().time()
    time1 = datetime.today()
    time1 = time1.strftime('%H:%M:%S')
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'сейчас {time1}')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'какое сегодня число' or speech == 'какое число сегодня':
    today = datetime.today()
    today = today.strftime('%d %m %Y') # ('%H %M %S') - часы минуты
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'сегодня {today}')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'кто самый лучший программист' or speech == 'какой программист самый лучший':
    n = 'самый лучший программист Никита Липский, псевдоним Никитиус Wolf'
    record1()
elif speech == 'что нового в танках':
    n = 'ожидаем хеллоуинские ивенты'
    record1()
elif speech == 'расскажи о себе' or speech == 'расскажи что-нибудь о себе':
    n = 'я программа написаная Никитиусом Wolf, могу отвечать на разные вопросы'
    record1()
elif speech == 'как сделать выход на одну':
    n = 'надо вывернуть руку'
    record1()
elif speech == 'когда у тебя день рождения' or speech == 'когда твой день рождения':
    n = 'мой день рождения тридцатого июля'
    record1()
elif speech == 'как дела' or speech == 'как у тебя дела' or speech == 'как дела у тебя':
    answers = ['у меня всё хорошо', 'у меня всё как обычно стою вот на столе на вопросы отвечаю', 'зарядка идёт значит всё хорошо' ]
    n = random.choice(answers)
    record1()
elif speech == 'кто делает самый вкусный торт рыжик' or speech == 'кто делает самый вкусный рыжик' or speech == 'у кого рыжик получается лучше всего' or speech == 'кто готовит самый вкусный торт рыжик' or speech == 'кто готовит лучший торт рыжик':
    n = 'лучше всех торт рыжик готовит Валентина Шитова'
    record1()
elif speech == 'столица россии' or speech == 'какая столица у россии' or speech == 'какая столица россии':
    n = 'столица России город Москва'
    record1()
elif speech == 'столица беларуси' or speech == 'столица белоруссии' or speech == 'какая столица белоруси':
    n = 'столица Белоруси город Минск'
    record1()
elif speech == 'столица сша' or speech == 'столица америки' or speech == 'какая столица америки':
    n = 'столица США город Вашингтон'
    record1()
elif speech == 'столица китая' or speech == 'столица кнр' or speech == 'какая столица китая':
    n = 'столица Китая город Пекин'
    record1()
elif speech == 'спасибо' or speech == 'спасибо тебе':
    n = 'не за что, обращайтесь'
    record1()
elif speech == 'курс доллара':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    today = datetime.today()
    today = today.strftime('%d/%m/%Y')
    url += str(today)
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    def get_course(id):
        return soup.find('valute', {'id': id}).value.text
    
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'{get_course("R01235")} рублей за 1 доллар\n')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'курс евро':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    today = datetime.today()
    today = today.strftime('%d/%m/%Y')
    url += str(today)
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    def get_course(id):
        return soup.find('valute', {'id': id}).value.text
    
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'{get_course("R01239")} рублей за 1 евро\n')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'курс юаня':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    today = datetime.today()
    today = today.strftime('%d/%m/%Y')
    url += str(today)
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    def get_course(id):
        return soup.find('valute', {'id': id}).value.text
    
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'{get_course("R01375")} рублей за 1 юань\n')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio8.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio8.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'сложи числа' or speech == 'сложить числа':
    n = 'сколько чисел хотите сложить'
    record1()
    record = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Скажите сколько чисел вы хотите сложить')
        audio = record.listen(source)
        speech = record.recognize_google(audio, language='ru_RU').lower()
        num = int(speech)

    numbers = []
    for nums in range(num):
        with sr.Microphone(device_index=1) as source:
            print('Назовите число...')
            audio = record.listen(source)
            speech = record.recognize_google(audio, language='ru_RU').lower()
            num = float(speech)
            numbers.append(num)
    num2 = sum(numbers)
    print(num2)
    n1 = int(num2)
    n2 = str(n1)
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write(f'сумма ваших чисел {n2}')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'найди синус':
    n = 'синус какого угла хотите найти'
    record1()
    record = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Скажите градус угла, синус которого хотите найти')
        audio = record.listen(source)
        speech = record.recognize_google(audio, language='ru_RU').lower()
        num = int(speech)
        num2 = sin(num)
        print(num2)
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write('синус угла в терминале')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'найди косинус':
    n = 'косинус какого угла хотите найти'
    record1()
    record = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Скажите градус угла, синус которого хотите найти')
        audio = record.listen(source)
        speech = record.recognize_google(audio, language='ru_RU').lower()
        num = int(speech)
        num2 = cos(num)
        print(num2)
    my_file = open('file2.txt', 'w', encoding='UTF-8')
    my_file.write('косинус угла в терминале')
    my_file.close()

    my_file = open('file2.txt', 'r', encoding='UTF-8')
    my_text = my_file.read()
    my_file.close()

    tts = gTTS(text=my_text, lang='ru')
    tts.save('audio.mp3')
    
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
elif speech == 'найди тангенс' or speech == 'найди катангенс':
    n = 'к сожалению в библиотеке math какие-то проблемы и данные от туда и из других источников могут расходиться'
    record1()
elif speech == 'что ты умеешь':
    n = 'я умею отвечать на вопросы'
    record1()
elif speech == 'уроки в понедельник' or speech == 'расписание на понедельник' or speech == 'уроки на понедельник' or speech == 'расписание в понедельник':
    n = 'в понедельник у вас по расписанию шесть уроков: география, английский, обществознание, обж, химия, алгебра'
    print('Уроки в понедельник:')
    print('1. География')
    print('2. Английский')
    print('3. Обществознание')
    print('4. ОБЖ')
    print('5. Химия')
    print('6. Алгебра')
    record1()
elif speech == 'уроки во вторник' or speech == 'расписание на вторник' or speech == 'уроки на вторник' or speech == 'расписание во вторник':
    n = 'во вторник у вас по расписанию семь уроков: литература, русский, английский, химия, информатика, физика, геометрия'
    print('Уроки во вторник:')
    print('1. Литература')
    print('2. Русский')
    print('3. Английский')
    print('4. Химия')
    print('5. Информатика')
    print('6. Физика')
    print('7. Геометрия')
    record1()
elif speech == 'уроки в среду' or speech == 'расписание на среду' or speech == 'уроки на среду' or speech == 'расписание в среду':
    n = 'в среду у вас по расписанию семь уроков: немецкий, физика, английский, литература, история, биология, алгебра'
    print('Уроки в среду:')
    print('1. Немецкий')
    print('2. Физика')
    print('3. Английский')
    print('4. Литература')
    print('5. История')
    print('6. Биология')
    print('7. Алгебра')
    record1()
elif speech == 'уроки в четверг' or speech == 'расписание на четверг' or speech == 'уроки на четверг' or speech == 'расписание в четверг':
    n = 'в четверг у вас по расписанию шесть уроков: '
    print('Уроки во вторник:')
    print('1. Литература')
    print('2. Русский')
    print('3. Английский')
    print('4. Химия')
    print('5. Информатика')
    print('6. Физика')
    print('7. Геометрия')
    record1()
elif speech == 'тестовый запуск':
    n = 'всё прошло успешно'
    record1()
else:
    n = 'похоже что данная функция не предусмотрена'
    record1()

# Алиса напомни мне (что-то записывать как заметку в файл и когда надо читать его)
# Погода
# Списки уроков по дням недели
# Угадай число
# Зарази компьютер
# Запусти игру
# Расскажи анекдот