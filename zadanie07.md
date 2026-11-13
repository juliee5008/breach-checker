# 1

Wszystkie:

breach-checker-frontend:przed (alpine 3.24.2)
=============================================
Total: 28 (HIGH: 27, CRITICAL: 1)

breach-checker-backend:dev (debian 13.7)
========================================
Total: 49 (HIGH: 49, CRITICAL: 0)

breach-checker-backend:prod (debian 13.7)
=========================================
Total: 49 (HIGH: 49, CRITICAL: 0)

breach-checker-frontend:prod (alpine 3.24.4)
============================================
Total: 3 (HIGH: 3, CRITICAL: 0)


Z poprawką:

breach-checker-frontend:przed (alpine 3.24.2)
=============================================
Total: 28 (HIGH: 27, CRITICAL: 1)

breach-checker-backend:dev (debian 13.7)
========================================
Total: 2 (HIGH: 2, CRITICAL: 0)

breach-checker-backend:prod (debian 13.7)
=========================================
Total: 2 (HIGH: 2, CRITICAL: 0)

breach-checker-frontend:prod (alpine 3.24.4)
============================================
Total: 3 (HIGH: 3, CRITICAL: 0)


--pull zmienił liczbe podatnosci tylo dla frontendu


# 2

backend-1  | FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/app']

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend touch /etc/test
touch: cannot touch '/etc/test': Read-only file system

What's next:
    Debug this Compose error with Gordon → docker ai "help me fix this compose error"
PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend touch /tmp/test
PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend grep CapEff /proc/1/status
CapEff: 0000000000000000

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend pytest
====================================================== test session starts ======================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0
rootdir: /app
collected 7 items

tests/test_check.py .......                                                                                               [100%]

======================================================= 7 passed in 0.07s =======================================================
PS C:\Users\lab04\jj_cyber\breach-checker>

Ustawienia dodane do docker-compose.yml zapobiegaja uzyskaniu przez proces backendu uprawnień roota i potencjalnie doprowadzenia do zmian w plikach na hoście w przypadku
błędu. 