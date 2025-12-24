import hashlib
import os
import sqlite3
import subprocess
from collections import defaultdict
from datetime import datetime

import numpy as np


def repo_root():
    # Корень репозитория — родительская папка для tests/
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def git_add_file(file_path):
    """Добавляет файл в отслеживаемые Git."""
    try:
        # Проверяем, находится ли файл в Git-репозитории
        git_dir = os.path.join(repo_root(), '.git')
        if not os.path.isdir(git_dir):
            return False, "Директория .git не найдена, возможно это не Git-репозиторий"

        # Выполняем команду git add для указанного файла
        result = subprocess.run(
            ['git', 'add', file_path],
            cwd=repo_root(),  # Устанавливаем рабочую директорию в корень репозитория
            check=False,  # Не вызываем исключение при ошибке
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return True, "Файл успешно добавлен в отслеживаемые"
        else:
            return False, f"Ошибка при добавлении файла: {result.stderr}"
    except Exception as e:
        return False, f"Исключение при работе с Git: {str(e)}"


def git_commit(message="Автоматическое обновление статуса заданий"):
    """Создает коммит с указанным сообщением."""
    try:
        # Проверяем, находится ли файл в Git-репозитории
        git_dir = os.path.join(repo_root(), '.git')
        if not os.path.isdir(git_dir):
            return False, "Директория .git не найдена, возможно это не Git-репозиторий"

        # Выполняем команду git commit
        result = subprocess.run(
            ['git', 'commit', '-m', message],
            cwd=repo_root(),  # Устанавливаем рабочую директорию в корень репозитория
            check=False,  # Не вызываем исключение при ошибке
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return True, "Коммит успешно создан"
        else:
            # Если нет изменений для коммита, это не ошибка
            if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
                return True, "Нет изменений для коммита"
            return False, f"Ошибка при создании коммита: {result.stderr}"
    except Exception as e:
        return False, f"Исключение при работе с Git: {str(e)}"


def db_path():
    # БД всегда в tests/result.db относительно корня репозитория
    return os.path.join(repo_root(), 'tests', 'result.db')


def create_new_db():
    os.makedirs(os.path.dirname(db_path()), exist_ok=True)
    with sqlite3.connect(db_path()) as connection:
        cursor = connection.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS test (
                                                           date_time   DATETIME,
                                                           task_number BIGINT,
                                                           task_type   INTEGER,
                                                           result      INTEGER
                       )
                       ''')


def add_result(date_time, task_number, task_type, result):
    if not os.path.exists(db_path()):
        create_new_db()
    with sqlite3.connect(db_path()) as connection:
        cursor = connection.cursor()
        # Проверяем, есть ли уже запись с таким task_number и task_type
        existing = get_result(task_number, task_type)
        
        # Если запись существует и последний результат был правильным (1), не добавляем новую запись
        if existing and existing[3] == 1:
            return  # Не добавляем дубликат правильного ответа
        
        # В остальных случаях добавляем новую запись
        cursor.execute('INSERT INTO test (date_time, task_number, task_type, result) VALUES (?, ?, ?, ?)',
                       (date_time, task_number, task_type, result))


def update_result(date_time, task_number, task_type, result):
    with sqlite3.connect(db_path()) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE test SET date_time = ?, result = ? WHERE task_type = ? AND task_number = ?',
                       (date_time, result, task_type, task_number))


def get_result(task_number, task_type):
    with sqlite3.connect(db_path()) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM test WHERE task_number = ? AND task_type = ?',
                       (task_number, task_type))
        return cursor.fetchone()


def get_results():
    with sqlite3.connect(db_path()) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM test')
        return cursor.fetchall()


def result_register(task_type, number, result, right_result):
    """
    Помечать файл задания, добавляя к имени файла в начало '+' или '-', соответственно.
    Оперделение пути файла проиходится через переменные task_type и number.
    Файлы располагаются в подпапке: Тема {task_type}/Задания/
    Имя файла: "Задание {number}.md" или "Задание {number}.png".
    """
    res = 1 if hashlib.md5(str(result).encode()).hexdigest() == right_result else 0
    # Храним дату в читабельном ISO-формате
    add_result(datetime.now().isoformat(), number, task_type, res)

    def mark_task_files(task_type, number, is_correct):
        """Ищет файлы задания (.md и .png и пр.) и переименовывает, добавляя префикс '+' или '-'"""
        try:
            t = int(task_type)
            n = int(number)
        except Exception:
            return []

        # Строим путь относительно корня репозитория, отталкиваясь от текущего файла tests/conftest.py
        task_dir = os.path.join(repo_root(), f"Тема {t}", "Задания")

        if not os.path.isdir(task_dir):
            task_dir = os.path.join(repo_root(), "ЕГЭ", f"Тема {t}", "Задания")
        if not os.path.isdir(task_dir):
            return []

        # Список поддерживаемых расширений файлов
        extensions = ['.md', '.png', '.py', '.jpg', '.ods', '.xlsx']
        sign = '+' if is_correct else '-'
        renamed = []

        for ext in extensions:
            base_name = f"Задание {n}{ext}"
            # Кандидаты: без префикса и с обоими префиксами
            candidates = [
                os.path.join(task_dir, base_name),
                os.path.join(task_dir, '+' + base_name),
                os.path.join(task_dir, '-' + base_name),
            ]

            src = None
            for cand in candidates:
                if os.path.exists(cand):
                    src = cand
                    break
            if not src:
                continue

            dst = os.path.join(task_dir, sign + base_name)
            try:
                if os.path.abspath(src) != os.path.abspath(dst):
                    os.replace(src, dst)  # перезаписываем, если существует файл с другим префиксом
                renamed.append(dst)
                success, message = git_add_file(dst)
                if not success:
                    print(f"Предупреждение при добавлении файла в Git: {message}")

            except Exception as e:
                print(f"Ошибка при переименовании файла: {str(e)}")

        return renamed

    mark_task_files(task_type, number, res == 1)
    success_commit, message_commit = git_commit(f"Обновлен статус задания {number} темы {task_type}. Задание решено {("Верно" if res else "Неверно")}")
    if not success_commit:
        print(f"Предупреждение при создании коммита: {message_commit}")
    return "Верно" if res else "Неверно"