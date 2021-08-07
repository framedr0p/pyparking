### pyparking
ist ein einfaches und leichtes System zum erfassen freier Parkplätze.
Die Anzahl der freien Parkplätze wird dabei auf einer Anzeigetafel vor dem Parkhaus wiedergegeben.


### Konfiguration des Raspi
am Raspi muss nur das Repo mit git clone kopiert werden und zwei Einträge in die crontab geschrieben werden.
```
@reboot sleep 30 && $(which python3) /pfad/zu/repo/pyparking/server.py > 2>&1
0 6 * * * sleep 30 && $(which python3) /pfad/zu/repo/pyparking/server.py > 2>&1
```

