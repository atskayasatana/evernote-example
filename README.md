# Взаимодействие с API Evernote.

В данном репозитории хранятся скрипты для работы с программой Evernote.
Для запуска понадобятся Python2.* и данные из песочницы Evernote.

## Регистрация в Evernote

Если нет аккаунта в Evernote, то переходим сюда https://sandbox.evernote.com/ и регистрируемся. 

Для работы понадобится персональный токен, его можно получить здесь:https://sandbox.evernote.com/api/DeveloperToken.action

Далее, в аккаунте можно создать несколько блокнотов и добавить туда заметки.

Туториал по работе с Evernote: https://help.evernote.com/hc/ru

![](https://github.com/atskayasatana/Images/blob/1b2a82d30d041434b58a9fbc0e303f144a517735/%D0%91%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82%D1%8B.png)

## Настройки пользователя

Перед началом работы нужно подготовить .env файл с настройками. В нём должны быть следующие данные:
``` Python
EVERNOTE_PERSONAL_TOKEN = # персональный токен разработчика
JOURNAL_NOTEBOOK_GUID = # id блокнота в который мы будем добавлять заметки
INBOX_NOTEBOOK_GUID = # id блокнота заметки из котрого мы будем выводить на экран
JOURNAL_TEMPLATE_NOTE_GUID = # шаблонная заметка, которую мы будем добавлять в блокнот
```
### EVERNOTE_PERSONAL_TOKEN 
Персональный токен пользователя, получить здесь:https://sandbox.evernote.com/api/DeveloperToken.action

### JOURNAL_NOTEBOOK_GUID 
Блокнот с которым мы будем работать. В своем аккаунте на https://sandbox.evernote.com/ заходим в выбранный блокнот.

Ссылка в браузере выглядит так:

![](https://github.com/atskayasatana/Images/blob/41b47b363a821c6df765e093d5a5f8eb51494a6f/bloknote_guid.png)

GUID блокнота это строка между b= и &, в данном случае 7021bded-e808-46eb-a4aa-6b0cc4546ba0

### INBOX_NOTEBOOK_GUID

Блокнот, информацию по которому мы хотим вывести на экран. Можно взять тот же GUID, что и в предыдущем пунтке, можно выбрать другой.

### JOURNAL_TEMPLATE_NOTE_GUID

Шаблонная заметка, которую мы будем добавлять в блокнот с GUID JOURNAL_NOTEBOOK_GUID.

GUID заметки можно получить аналогично GUID блокнота. 

Переходим в заметку, в адресной строке GUID заметки находится между n= и &

![](https://github.com/atskayasatana/Images/blob/bc8aeeb6b91c8be13117c5a21c049b1bbfed012e/note_guid.png)

В примере выше это 6446f9b5-6c97-49f6-a85c-86d08a10aa04

## Запуск скриптов

Все скрипты написаны для Python2, соответсвенно нужно создать окружение с такой же версией Python:
```
conda create -n имя_окружения python=2.7
```

Для работы нам понадобятся библиотеки из файла requirements.txt

```
pip install -r requirements.txt
```
### list_notebooks.py

Скрипт позволяет посмотреть список всех блокнотов пользователя.

```
python list_notebooks.py
```








