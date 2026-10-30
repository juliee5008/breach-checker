# 1

 ✔ Container breach-checker-db-1       Healthy                                                                                                                               5.9s
 ✔ Container breach-checker-backend-1  Healthy                                                                                                                              36.5s
 ✔ Container breach-checker-frontend-1 Started                                                                                                                              36.6s
PS C:\Users\lab04\jj_cyber\breach-checker>

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose ps
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED         STATUS                        PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    2 minutes ago   Up About a minute (healthy)   5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         2 minutes ago   Up 2 minutes (healthy)        5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   2 minutes ago   Up About a minute             0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
PS C:\Users\lab04\jj_cyber\breach-checker>

# 2

Po insert:
PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec db psql -U breach -d breachdb -c "INSERT INTO leaked_hashes VALUES ('bc45408273d7e1914b741c3407b0b559764f7876');"
INSERT 0 1
PS C:\Users\lab04\jj_cyber\breach-checker> '{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '@-'
{"found":true}

Po down+up:
{"found":true}

Po down -v + up"
{"found":false}

Skrót przerwał down ponieważ dane bazy zostały zapisane w wolumenie. Wolumen został usuniety dopiero po down -v, dlatego skrót nie przetrwał. 
Po down -v w bazie znów jest 89 skrótów ponieważ baza została utworzona od zera na podstawie init.sql.

# 3

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose ps
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED              STATUS                        PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    About a minute ago   Up About a minute (healthy)   5000/tcp
breach-checker-backend-2    breach-checker-backend    "python app.py"          backend    About a minute ago   Up About a minute (healthy)   5000/tcp
breach-checker-backend-3    breach-checker-backend    "python app.py"          backend    About a minute ago   Up About a minute (healthy)   5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         About a minute ago   Up About a minute (healthy)   5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   About a minute ago   Up 46 seconds                 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec frontend nslookup backend
Server:         127.0.0.11
Address:        127.0.0.11:53

Non-authoritative answer:

Non-authoritative answer:
Name:   backend
Address: 172.19.0.3
Name:   backend
Address: 172.19.0.4
Name:   backend
Address: 172.19.0.5

Przed restarem frontendu:

backend-2  | 127.0.0.1 - - [30/Oct/2026 13:32:17] "GET /health HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.6 - - [30/Oct/2026 13:32:18] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.6 - - [30/Oct/2026 13:32:18] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.6 - - [30/Oct/2026 13:32:18] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.6 - - [30/Oct/2026 13:32:18] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...

Po restarcie frontendu:

backend-2  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-1  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-3  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.6 - - [30/Oct/2026 13:36:08] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...

Przed restartem frontend nie znał innych adresów replik backendu, dlatego kierował zapytania do jednego. 
Skalowanie byłoby niemozliwe z ports: "5000:5000" ponieważ wtedy każda replika chciałaby nasłuchiwac na tym samym porcie hosta na co system nie pozwala

