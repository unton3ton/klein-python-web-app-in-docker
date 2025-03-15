# Выбор базового образа с Python
FROM python:3.8-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов проекта
COPY . /app

# Установка зависимостей
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открытие порта для взаимодействия с приложением
EXPOSE 9000

# Запуск приложения
CMD ["python3", "./app/app.py"]