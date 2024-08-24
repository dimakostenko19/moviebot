# MovieBot

MovieBot — это Telegram-бот, построенный с использованием библиотеки Aiogram. Этот бот позволяет пользователям искать фильмы по коду и предоставляет панель администратора, где администраторы могут добавлять, удалять, обновлять и просматривать все фильмы.

## Функциональность

- **Поиск фильма по коду**: Пользователи могут искать фильм, используя его уникальный код.
- **Админ-панель**:
  - Добавление нового фильма в базу данных.
  - Удаление фильма по его коду.
  - Обновление кода и названия существующего фильма.
  - Просмотр всех фильмов, хранящихся в базе данных.
  - Рассылка сообщений
- **Доступ к боту**: Для доступа к боту пользователью нужно подписаться на телеграм канал.
## Установка

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/dimakostenko19/moviebot.git
    cd MovieBot
    ```

2. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Настройте файл `config.py`** с вашим токеном бота и учетными данными базы данных:

4. **Запустите бота**:
    ```bash
    python main.py
    ```

## Использование

- **Поиск фильма**: Отправьте боту код фильма, и он вернет название фильма.
  
- **Команды администратора**:
  - **Добавить фильм**: Команда для добавления фильма, указав его код и название.
  - **Удалить фильм**: Укажите код фильма, чтобы удалить его из базы данных.
  - **Обновить фильм**: Обновите код и название существующего фильма.
  - **Просмотреть все фильмы**: Показать список всех фильмов в базе данных.
  - **Рассылка сообщения**: Администраторы могут отправлять заготовленые сообщения всем пользователям.

![menu_img](https://github.com/user-attachments/assets/013ceaa1-6045-4126-9f57-840852f40592)
## Структура проекта

```plaintext
.
├── kino_bot/
│   ├── handlers/
│   │   ├── admin_handlers.py
│   │   ├── user_handlers.py
│   ├── data/
│   │   ├── db.py
│   ├── keyboards/
│   │   ├── admin_keyboard.py
│   │   ├── keyboard.py
│   ├── main.py
├── requirements.txt
├── config.py
├── README.md
