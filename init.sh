sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/guniconf-hello.conf   /etc/gunicorn.d/guniconf_hello
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /etc/gunicorn.d/guniconf_hello hello:wsgi_application
