# Описание проекта

![image](https://user-images.githubusercontent.com/47640060/132115529-d35223b0-8c29-4772-896e-04ff3b57024b.png)

## [Api](https://github.com/keworr/accenture-case/blob/main/api.py)
1) Основная функция - ребалансировка портфеля. Анализ структуры портфеля и его соответствия целям пользователя; в случае несоответствия - индивидуальные рекомендации с объяснениями.
2) Получение информации по акциям через публичный api (график цен, капитализация, дивидендные даты и т.п.) и расчёты (волатильность)
3) Рекомендации похожих акций (по волатильности)
4) Целевая цена акции (средние прогнозы фондов по целевой цене акции)

## [Frontend](https://github.com/keworr/accenture-case/tree/front)
Фронтенд часть проекта

## [Дизайн](https://www.figma.com/file/mePF97DJRCa9Pf0B0vNpCW/Accenture-Investement?node-id=20%3A173)
Дизайн проекта

## [База данных sqlite](db.db)
Структура данных в БД:
- users (user_id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, fullname TEXT, invest_type INTEGER);
- assets (id INTEGER PRIMARY KEY, user_id INTEGER, stocks TEXT, count INTEGER, FOREIGN KEY(user_id) REFERENCES users(user_id));
- stocks (id INTEGER PRIMARY KEY, stocks TEXT, volatility REAL, caps REAL);

## [Веб-сервер на python (bottle)](bottle_app.py)
Небольшой веб-сервер, связывающий api.py с фронтендом для демонстрации решения (запущен на хостинге). 

Запуск:<br>
`python3 bottle_app.py`
