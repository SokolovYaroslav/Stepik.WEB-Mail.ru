sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
sudo gunicorn -c /home/box/web/etc/guniconf-hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/guniconf-django.py ask.wsgi:application
