# Взаимодействие с API Evernote.

В данном репозитории хранятся скрипты для работы с программой Evernote.

Для запуска понадобятся Python2.* и данные из песочницы Evernote.

## Регистрация в Evernote

Если нет аккаунта в Evernote, то переходим сюда https://sandbox.evernote.com/ и регистрируемся. 

Для работы нужен персональный токен, его можно получить здесь:https://sandbox.evernote.com/api/DeveloperToken.action

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
###### EVERNOTE_PERSONAL_TOKEN 
Персональный токен пользователя, получить здесь:https://sandbox.evernote.com/api/DeveloperToken.action

###### JOURNAL_NOTEBOOK_GUID 
Блокнот с которым мы будем работать. В своем аккаунте на https://sandbox.evernote.com/ заходим в выбранный блокнот.

Ссылка в браузере выглядит так:

![](https://github.com/atskayasatana/Images/blob/41b47b363a821c6df765e093d5a5f8eb51494a6f/bloknote_guid.png)

GUID блокнота это строка между b= и &, в данном случае 7021bded-e808-46eb-a4aa-6b0cc4546ba0

###### INBOX_NOTEBOOK_GUID

Блокнот, информацию по которому мы хотим вывести на экран. Можно взять тот же GUID, что и в предыдущем пункте, можно выбрать другой.

###### JOURNAL_TEMPLATE_NOTE_GUID

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
Активируем новое окружение:

```
conda activate имя_окружения

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
Пользователь увидит список своих блокнотов и их GUID

![](https://github.com/atskayasatana/Images/blob/470e360b2b7da8f0160bb96ab5217c1842fd4b0c/list_notebooks.png)

### dump_inbox.py 

Скрипт выводит содержимое заметок выбранного блокнота, в файле настроек это блокнот с  INBOX_NOTEBOOK_GUID.

Заметки выводятся отсортированные в обратном порядке по времени обновления, от самой свежей к старым. 

Количество заметок для вывода задается при вызове функции, по умолчанию выводится 10 последних.

```
python dump_inbox.py [число заметок для отображения]

```
![](https://github.com/atskayasatana/Images/blob/7c752d24e3eeac5799a5d1d5795b4d31b4256ecc/dump_inbox.png)

### add_note2journal.py

Скрипт для добавления заметки в блокнот с GUID = JOURNAL_NOTEBOOK_GUID. 

Пользователь при запуске скрипта задает дату заметки и в блокноте появляется новая заметка с указанной датой и содержимым заметки-шаблона. Если дата не указана, то заметка будет от текущей даты.

```
python add_note2journal.py [YYYY-MM-DD]
```

Если скрипт отработал, то появляется сообщение о создании новой заметки в блокноте
![](https://github.com/atskayasatana/Images/blob/f60c4feb11a98c1707b84790c4ae11434192ca87/add_note2journal.png)

## Функции
### def is_valid_date(text)

Преобразует аргумент text в объект datetime, если такое преобразование возможно.
Если text вместо даты в формате YYYY-MM-DD содержит +/-число или просто число, то функция вернет текущую дату + число дней.
Если text никак в дату преобразовать нельзя, то вернется сообщение об ошибке.

### get_notebook_list(note_store, notebook_guid, number=10, offset=0)

Возвращает данные о заметках блокнота notebook_guid из всех блокнотов пользователя note_store. 
Данные возвращаются в виде особой структуры, т.н. мета данных c помощью встроенной функции findNotesMetadata.

## config.py

Файл с настройками, содержит описание класса Settings, объекты которого используются во всех скриптах.
Класс хранит все необходимые для работы настройки из .env файла.














