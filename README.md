# Автоматизация Docker с помощью Ansible

Этот проект автоматизирует установку Docker и выполнение скриптов с использованием Ansible.

## Структура

- `install_docker.yml`: Устанавливает Docker и добавляет текущего пользователя в группу `docker`.
- `check_scripts.yml`: Собирает Docker-образ, запускает контейнер со скриптами и проверяет логи.
- `http_script.sh`: Bash-скрипт для запуска Python-скрипта.
- `http_script.py`: Python-скрипт для выполнения HTTP-запросов.
- `Dockerfile`: Определяет Docker-образ на базе Ubuntu 22.04 с необходимыми зависимостями.

## Требования

- Установленный Ansible на хосте.
- Доступ в интернет для установки пакетов.
- Среда, совместимая с Docker.

## Использование

1. **Установка Docker:**
   ```bash
   ansible-playbook -i "localhost," -c local install_docker.yml
   ```

2. **Проверка скриптов:**
   ```bash
   ansible-playbook -i "localhost," -c local check_scripts.yml
   ```

   - В логах отобразятся результаты HTTP-запросов и сообщение об успешном выполнении.