# GitHub Search UI Tests

UI-автотест проверяет сценарий глобального поиска GitHub:

1. Открыть `https://github.com`.
2. Найти поле поиска.
3. Ввести `copilot` и запустить поиск.
4. Найти в выдаче репозиторий `CopilotKit/CopilotKit`.
5. Перейти на страницу репозитория.
6. Проверить, что в README.md отображается текст `CopilotKit`.

Проект реализован на Python, PyTest и Playwright с использованием паттерна Page Object Model.

## Стек

- Python >= 3.12
- Playwright == 1.55.0
- PyTest == 8.4.1
- Браузер: Chrome
- IDE: PyCharm

## Структура проекта

```text
github_search_ui_tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── github_home_page.py
│   ├── repository_page.py
│   └── search_results_page.py
├── tests/
│   └── test_github_search.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка и запуск через терминал

### 1. Клонировать репозиторий

```bash
git clone <https://github.com/Danevil1/github_search_ui_tests>
cd github_search_ui_tests
```

### 2. Создать виртуальное окружение

#### macOS / Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Установить Chrome для Playwright

```bash
python -m playwright install chrome
```

### 5. Запустить тесты в headless-режиме

```bash
pytest
```

### 6. Запустить тесты с открытым окном браузера

#### macOS / Linux

```bash
HEADLESS=false pytest
```

#### Windows PowerShell

```powershell
$env:HEADLESS="false"; pytest
```

## Запуск из PyCharm

1. Открыть папку проекта `github_search_ui_tests` в PyCharm.
2. Создать виртуальное окружение Python 3.12 или выбрать уже созданное `.venv`.
3. Установить зависимости из `requirements.txt`.
4. Выполнить команду `python -m playwright install chrome` в терминале PyCharm.
5. Открыть файл `tests/test_github_search.py`.
6. Нажать Run рядом с тестом `test_user_can_find_copilotkit_repository_from_global_search`.

## Архитектура

Используется Page Object Model:

- `GitHubHomePage` - главная страница GitHub и глобальный поиск.
- `SearchResultsPage` - страница поисковой выдачи и переход к репозиторию.
- `RepositoryPage` - страница репозитория и проверка README.md.
- `BasePage` - общие методы для работы со страницей и XPath-локаторами.

Основная часть элементов ищется через XPath. Локаторы сделаны устойчивыми к небольшим изменениям верстки: используются частичные совпадения атрибутов, текста и классов.


## Тест-кейс

Ссылка на Google Docs: **https://docs.google.com/document/d/1pEPmAGVB1XaEhykpGmUBdbUI3-y7MTLYwQhvhZe7ZbE/edit?usp=sharing**.
