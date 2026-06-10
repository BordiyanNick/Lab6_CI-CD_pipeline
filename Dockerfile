# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

FROM python:3.10-slim

WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо файл зі скриптом
COPY . .
EXPOSE 5000

# Команда для запуску скрипта
CMD ["python", "main.py"]
