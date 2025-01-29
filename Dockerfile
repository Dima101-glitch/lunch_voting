# Використовуємо офіційний Python-образ
FROM python:3.10

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли в контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт 8000
EXPOSE 8000

# Запускаємо сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
