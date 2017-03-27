sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pip3 install --upgrade django
sudo gunicorn -c /home/box/web/etc/guniconf-hello.py hello:wsgi_application
cd ask/
sudo gunicorn -c /home/box/web/etc/guniconf-django.py ask.wsgi:application
