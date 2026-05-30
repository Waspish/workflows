# GitHub Actions Workflows

Примеры использования **GitHub Actions** для автоматического запуска Selenium-тестов на браузере Safari в операционной системе macOS.

## 🔧 Как это работает

1. **Файл workflow** (`.github/workflows/selenium-safari.yml`) содержит инструкции для GitHub Actions:
   - Запускается на событиях `push` и `pull_request` в ветку `master`.
   - Выполняется на раннере `macos-latest`.
   - Устанавливает Python 3.10, зависимости из `requirements.txt`.
   - Запускает Python-скрипт `test.py`.

2. **Python-скрипт** (`test.py`) выполняет простой Selenium-тест:
   - Открывает браузер Safari.
   - Переходит на сайт `https://www.saucedemo.com/`.
   - Выводит в консоль заголовок страницы.

## 🚀 Запуск вручную

Проект рассчитан на автоматический запуск в CI. Но при желании вы можете выполнить тест локально (на компьютере с macOS):

```bash
# Клонирование репозитория
git clone https://github.com/Waspish/workflows.git
cd workflows

# Создание виртуального окружения
python -m venv .venv
source .venv/bin/activate      # macOS
# или .venv\Scripts\activate   # Windows (но Safari недоступен)

# Установка зависимостей
pip install -r requirements.txt

# Запуск теста
python test.py
```

> **Важно:** Локальный запуск возможен только на **macOS**, так как Safari и его WebDriver не доступны на других платформах.

## 🛠 Используемые технологии

- **GitHub Actions** – CI/CD платформа.
- **Selenium WebDriver** – автоматизация браузера.
- **Python 3** – язык реализации теста.
- **macOS runner** – среда выполнения с нативным Safari.
