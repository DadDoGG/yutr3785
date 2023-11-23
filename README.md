# Инструкцией по развертыванию

<h2>Установка проекта </h2>
Клонирвоанеи проекта с гита<br>
<code>git clone https://github.com/DadDoGG/yutr3785.git </code><br>
Установка нужной версии питона<br>
<code>sudo apt install python3.12 python3.12-dev python3.12-venv</code><br>
Создание виртуального окружения и установка зависимостей <br>
<code> python3.12 -m venv venv </code> <br>
<p><code>. venv/bin/activate</code></p>
<p><code>pip install -r requirements.txt</code></p>
<p> Создайте <b>.env</b> файл который будет иметь структуру <b><br>DB_NAME=test<br>
DB_USER=test<br>
DB_PASSWORD=test<br>
DB_HOST=test<br></b></p>

<p>Далее выполните миграции с помощью команды: <br><code>python manage.py migrate</code><br> <code>python manage.py runserver</code></p>

<h2>uWSGI</h2>
<p>Для начала нужно создать конфиг файл для uWSGI.<br>Шаблон конфига для uWSGI находиится в файле  <b>yutr_uwsgi.ini</b> </p>
После создание файла можно проверить его запустив команду<br>
<code>uwsgi --http :8000 --module yutr.wsgi</code>
и перейдя на 8000 порт можно увидеть резузьтат
<h3>Создание Служебного сервиса uWSGI</h3>
<p>Служебный сервис нужен чтобы не нужно было руками каждый раз запускать сервис и он автоматически запускался вместе с Ubuntu </p>
<p>Для этого создайте <b>someapp.service</b> файл по шаблону файла <b>uwsgi_service_example</b>. 
Потом скопируйте его в диеркторию <b>systemd</b> с помощью команды <br>
<code>sudo cp someapp.service /etc/systemd/system/</code>
И запутстите его с помощью команд: <br> <code>sudo systemctl start someapp</code><br><code>sudo systemctl enable someapp</code></p>

NOTE: Для этого нужно поставить глобально себе <b>uwsgi</b>

<h2>Nginx</h2>
Для начала нужно установить nginx с помощью команды:<br>
<code>sudo apt-get install nginx </code><br>
<p>Проверить установился ли он можно с помощью команды <code>nginx -v</code></p>

<p>Далее создаем файл конфигурации
<code>sudo nano /etc/nginx/sites-available/someapp</code> по шаблону в фалйе <b>yutr_nginx.conf</b>
<br>
И активируем конфигурацию с помощью команды <code> sudo ln -s /etc/nginx/sites-available/someapp /etc/nginx/sites-enabled </code>

И перезапускаем Nginx с помощью команды <code>sudo systemctl restart nginx</code>

