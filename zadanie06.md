# zad 1

z lower():

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items

tests/test_check.py::test_leaked_hash_is_found PASSED                                                                                                                    [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                                                                               [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                                                                                      [ 42%]
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                                                                          [ 57%]
tests/test_check.py::test_leaked_hash_upper_is_found PASSED                                                                                                              [ 71%]
tests/test_check.py::test_request_not_json PASSED                                                                                                                        [ 85%]
tests/test_check.py::test_hash_39_characters PASSED                                                                                                                      [100%]

============================================================================== 7 passed in 0.07s ===============================================================================
PS C:\Users\lab04\jj_cyber\breach-checker>

bez lower():

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose exec backend pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items

tests/test_check.py::test_leaked_hash_is_found PASSED                                                                                                                    [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                                                                               [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                                                                                      [ 42%]
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                                                                          [ 57%]
tests/test_check.py::test_leaked_hash_upper_is_found FAILED                                                                                                              [ 71%]
tests/test_check.py::test_request_not_json PASSED                                                                                                                        [ 85%]
tests/test_check.py::test_hash_39_characters PASSED                                                                                                                      [100%]

=================================================================================== FAILURES ===================================================================================
_______________________________________________________________________ test_leaked_hash_upper_is_found ________________________________________________________________________

client = <FlaskClient <Flask 'app'>>

    def test_leaked_hash_upper_is_found(client):
        response = client.post("/check", json={"hash": LEAKED.upper()})
>       assert response.status_code == 200
E       assert 400 == 200
E        +  where 400 = <WrapperTestResponse streamed [400 BAD REQUEST]>.status_code

tests/test_check.py:27: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED tests/test_check.py::test_leaked_hash_upper_is_found - assert 400 == 200
========================================================================= 1 failed, 6 passed in 0.11s ==========================================================================

What's next:
    Debug this Compose error with Gordon → docker ai "help me fix this compose error"

Testy z zajec nie wykryly usuniecia lower() poniewaz ..........


# ZAD 2

PS C:\Users\lab04\jj_cyber\breach-checker> '{"hash":"7c4a8d09ca3762af61e59520943dc26494f8941b"}' | curl.exe -s -o blad.html -w "HTTP %{http_code}\n" -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '@-'
HTTP 500

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose ps -a
NAME                        IMAGE                                                                     COMMAND                  SERVICE    CREATED          STATUS                                     PORTS
breach-checker-backend-1    breach-checker-backend                                                    "flask --app app run…"   backend    48 minutes ago   Up Less than a second (health: starting)   5000/tcp
breach-checker-db-1         postgres:16-alpine                                                        "docker-entrypoint.s…"   db         48 minutes ago   Exited (0) About a minute ago
breach-checker-frontend-1   sha256:10ead04b53306c5cc9d234dac57402049043156f98ced3558f34af8e36928793   "/docker-entrypoint.…"   frontend   57 minutes ago   Up 56 minutes                              0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
PS C:\Users\lab04\jj_cyber\breach-checker> docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' breach-checker-backend-1
running 0

po kilku sekundach:

PS C:\Users\lab04\jj_cyber\breach-checker> docker compose ps -a
NAME                        IMAGE                                                                     COMMAND                  SERVICE    CREATED          STATUS                          PORTS
breach-checker-backend-1    breach-checker-backend                                                    "flask --app app run…"   backend    49 minutes ago   Exited (1) About a minute ago
breach-checker-db-1         postgres:16-alpine                                                        "docker-entrypoint.s…"   db         49 minutes ago   Exited (0) 2 minutes ago
breach-checker-frontend-1   sha256:10ead04b53306c5cc9d234dac57402049043156f98ced3558f34af8e36928793   "/docker-entrypoint.…"   frontend   58 minutes ago   Up 57 minutes                   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
PS C:\Users\lab04\jj_cyber\breach-checker> docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' breach-checker-backend-1
exited 1

tu: w porownaniu z krokiem 4 w docker compose ps widoczny tylko frontend z cpu 0%, w logach backendu informacja o niemozliwosci polaczenia z db, klient dostal blad.html

Blad.html zawieral duzo informacji dot bledow w kodzie wraz z fragemntami kodu i sciezkami (traceback),  przez co zwykly uzytkownik moze poznac szczegoly np komunikacji z bazą ktora moze zawierac dane wrazliwe i w ten sposob powstaje podatnosc

# zad 3

Przed poprawką:

server {
    listen 80;

    # Pliki strony (index.html, style.css, script.js)
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    # Wszystko pod /api/ nginx przekazuje do usługi backend w sieci Compose
    location /api/ {
        proxy_pass http://backend:5000/;
    }
}


Po poprawce:

HTTP/1.1 404 Not Found
Server: nginx/1.31.6
Date: Wed, 11 Nov 2026 10:32:44 GMT
Content-Type: text/html
Content-Length: 153
Connection: keep-alive

W obrazie produkcyjnym, jak widać w Dockerfile, kopiujemy do katalogu /html tylko pliki związane ze stroną (index style script),
podobnie jak po poprawce w zadaniu. Kopiowanie całego katalogu projektu do katalogu serwerowanego jest ryzykowne, ponieważ udostępnia się użytkownikom do wglądu wszystkie pliki projektu, w tym te zawierajace poufne dane.

