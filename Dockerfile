# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

FROM python:3.10-slim

WORKDIR /app

# Встановлюємо необхідні бібліотеки безпосередньо через pip
RUN pip install --no-cache-dir numpy scipy matplotlib

# Копіюємо файл зі скриптом
COPY main.py .

# Команда для запуску скрипта
CMD ["python", "main.py"]
