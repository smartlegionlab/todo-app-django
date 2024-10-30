# ToDo App Web (Django)

---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/todo_app_web_django)](https://github.com/smartlegionlab/todo_app_web_django/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/todo_app_web_django)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/todo_app_web_django)](https://github.com/smartlegionlab/todo_app_web_django/blob/master/LICENSE)

---

**TODO App** is a web application developed using the Django framework that allows users to efficiently manage their tasks. The application provides an intuitive interface for creating, editing, and deleting tasks, as well as tracking their status.

#### Key Features:

- **Task Creation**: Users can add new tasks with a title, description, due date, and priority level.
- **Task Management**: Tasks can be edited, marked as completed, or deleted.
- **Filtering and Sorting**: Users can filter tasks by status (completed/incomplete) and sort them by creation date or priority.
- **Task Priorities**: Each task can have one of three priority levels (high, medium, low), helping users focus on the most important tasks.
- **Responsive Interface**: The application features a modern and responsive design, ensuring convenient access from various devices.

TODO App on Django is the perfect solution for those looking to organize their tasks and enhance productivity in their daily lives.

---

## Other applications:

- [Console ToDo app](https://github.com/smartlegionlab/todo_app_cli/)
- [Desktop ToDo app](https://github.com/smartlegionlab/todo_app_desktop/)
- [Telegram bot - ToDo app](https://github.com/smartlegionlab/todo_app_tg_bot/) | [Use](https://t.me/smarttodoappbot)

---

## Help:

### MariaDb:

- `sudo systemctl stop mysqld`
- `sudo pacman -S mariadb libmariadbclient mariadb-clients`
- `sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`
- `sudo systemctl start mariadb`
- `sudo mysql_secure_installation`
- `sudo systemctl restart mariadb`
- `sudo mysql -u root -p`

- `CREATE USER 'USER_NAME'@'localhost' IDENTIFIED BY 'PASSWORD';`
- `CREATE DATABASE database_name CHARACTER SET utf8 COLLATE utf8_general_ci;` or `CREATE DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`
- `GRANT ALL PRIVILEGES ON database_name.* TO 'USER_NAME'@'localhost';`
- `FLUSH PRIVILEGES;`
- `exit`



- Clone project
- Go to the project folder

### Requirements:

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`


### Create file in project folder: .env:

```env
TODO_APP_WEB_SECRET_KEY="<your django secret key>"
TODO_APP_WEB_DB_NAME="todo_app_web_db"
TODO_APP_WEB_DB_USER="todo_app_web_user"
TODO_APP_WEB_DB_PASSWORD="<password>"
TODO_APP_WEB_DB_HOST="localhost"
```


## Run:

- `python manage migrate`
- `python manage createsuperuser`
- `python manage.py runserver`
- Open in browser [link](http://127.0.0.1:8000)

---

## Images:

![logo](https://github.com/smartlegionlab/todo_app_web_django/raw/master/data/images/logo.png)

---

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
