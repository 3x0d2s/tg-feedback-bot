# tg-feedback-bot

Status: in development

<!-- PROJECT LOGO -->
<p align="center">
  <h3 align="center">tg-feedback-bot</h3>
  <p align="center">
    Чат-бот для самых разных сервисов!
  </p>
  <p align="center">
    <a href="https://github.com/3x0d2s/chatbot-tech-support/issues">Сообщить об ошибках</a>
  </p>
</p>

<br />

<!-- ABOUT THE PROJECT -->

## О проекте

Проект представляет собой реализацию быстрой, удобной и динамической техподдерки, которая базируется в месседжере Telegram.
Чат-бот работает полностью асинхронно, что существенно повышает кол-во одновременно обрабатываемых пользователей.

### Как это устроено?

У человека, пользующегося вашими услугами, может возникнуть вопрос, просьба или предложение. В таком случае, чтобы связаться с бизнесом, ему следует запустить приложение Telegram на своём устройстве и написать в чат-боту, затем он автоматически свяжет этого человека с свободным оператором, между ними будет организован диалог, в котором они будут общаться.

### Разработано с помощью

- [aiogram](https://github.com/aiogram/aiogram)

<!-- GETTING STARTED -->

## Начало работы

Это пример того, как вы можете локально настроить проект. Чтобы запустить бота, следуйте этим простым указаниям.

1. Клонируйте репозиторий и перейдите в его директорию
   ```sh
   $ git clone https://github.com/3x0d2s/tg-feedback-bot.git
   $ cd chatbot-tech-support
   ```
2. Скопируйте файл `example.env` в файл `.env`
   ```sh
   $ cp example.env .env
   ```
3. Откройте и заполните файл `.env` (у вас должна быть запущена БД PostgreSQL)
4. Разверните виртуальное окружение Python:
   ```sh
   $ python3 -m venv env
   $ source env/bin/activate
   ```
5. Установите необходимые библиотеки:
   ```sh
   $ pip3 intall -r requirements.txt
   ```
6. Создание структуры БД:
  ```sh
  $ python3 tgbot/data/sql.py
  ```
7. Запуск:
   ```sh
   $ python3 bot.py
   ```


## Лицензия

Распространяется по лицензии MIT. См. `LICENSE.md` для дополнительной иформации.

<!-- CONTACT -->

## Контакты

Максим Жданов - [@ex0d2s](https://t.me/ex0d2s)
