# 1

{"status":"ok"}
172.18.0.1 - - [23/Oct/2026 12:45:07] "GET /health HTTP/1.1" 200 -


# Zad dokończone po zajęciach:
 
# 2

PS C:\Users\Julia\mw\lab4\breach-checker> docker run --rm --network breach-net healthcheck-probe
backend: OK
PS C:\Users\Julia\mw\lab4\breach-checker> docker run --rm healthcheck-probe
backend: UNREACHABLE
PS C:\Users\Julia\mw\lab4\breach-checker> docker stop backend
backend
PS C:\Users\Julia\mw\lab4\breach-checker> docker run --rm --network breach-net healthcheck-probe
backend: UNREACHABLE

Uruchamiając healthcheck bez --network probuje on połączyć się z backendem w sieci domyslnej Dockera, w ktorej abckend sie nie znajduje

# 3
PS C:\Users\Julia\mw\lab4\breach-checker> docker restart backend
backend
PS C:\Users\Julia\mw\lab4\breach-checker> docker exec backend cat /tmp/notatka.txt
notatka

PS C:\Users\Julia\mw\lab4\breach-checker> docker exec backend cat /tmp/notatka.txt
cat: /tmp/notatka.txt: No such file or directory

PS C:\Users\Julia\mw\lab4\breach-checker> docker run --rm -v breach-dane:/dane alpine sh -c "date >> /dane/historia.txt; cat /dane/historia.txt"
Fri Oct 30 09:29:41 UTC 2026
Fri Oct 30 09:29:52 UTC 2026

Każdy kontener ma warstwę zapisywalną, w której lądują zmiany plików i logi; nie jest usuwana przy zatrzymaniu kontenera, ale kasuje się razem z kontenerem, dlatego notatka.txt nie przetrwała usunięcia i ponownego uruchomienia kontenera. Natomiast historia.txt przetrwała wyłączenie kontenera, ponieważ została zapisana w wolumenie istniejącym niezależnie od kontenera.
Lista wycieków przeżyłaby docker rm ponieważ jej zawartość jest zapisana na dysku hosta i jedynie udostępniana kontenerowi przez bind mount.