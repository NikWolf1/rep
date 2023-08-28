# голосовой калькулятор

import pygame
from gtts import gTTS
import speech_recognition as sr

numbers = []

record = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print('Скажите первое число:')
    audio = record.listen(source)
speech = record.recognize_google(audio, language='ru_RU').lower()
numbers.append(speech)

record = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print('Скажите второе число:')
    audio = record.listen(source)
speech = record.recognize_google(audio, language='ru_RU').lower()
numbers.append(speech)

number = sum(numbers)

my_file = open('some.txt', 'w', encoding='UTF-8')
my_file.write(number)
my_file.close()

my_file = open('some.txt', 'r', encoding='UTF-8')
my_text = my_file.read()
my_file.close()

tts = gTTS(text=my_text, lang='ru') # синтезирует текст в аудиоформат
tts.save('audio.mp3') # сохраняет резульат в mp3 файл

pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.event.poll