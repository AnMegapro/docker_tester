import time
from datetime import datetime

print("Запуск программы - вывод времени каждые 5 секунд")
print("Нажмите Ctrl+C для остановки")
print("-" * 50)

try:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Текущее время: {current_time}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем")
