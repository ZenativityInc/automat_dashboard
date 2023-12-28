# FMT_visualization_dashboard

For future update:
*in Linux:
1.cd into FMT_visualization_dashboard/ - Delete staticfiles/ folder

2.conda activate GUI

3.python manage.py collectstatic

4.cd into cronjob/ - Delete the cronjob process

5. run the crontab -e again


For running the program

```
waitress-serv --listen=192.168.1.91:8888 GUI.wsgi.application
```