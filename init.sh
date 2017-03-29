sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database web_proj_db;"
sudo mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'qwerty123';"
sudo mysql -uroot -e "GRANT ALL ON dj.* TO 'django@localhost';"
sudo mysql -uroot -e "GRANT USAGE ON *.* TO 'django@localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
sudo gunicorn -c /home/box/web/etc/guniconf-hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/guniconf-django.py ask.wsgi:application
