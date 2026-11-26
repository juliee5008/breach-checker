# 8.1

Z błędem:

https://github.com/juliee5008/breach-checker/actions/runs/45885199647

ERROR: failed to build: failed to solve: process "/bin/sh -c htmlhint index.html" did not complete successfully: exit code: 1

Po poprawce:

https://github.com/juliee5008/breach-checker/actions/runs/45886015295

Wcześniej z rejestru pobierany był tylko gotowy obraz backendu, a frontend budowany byl dopiero podczas weryfikacji

# 8.2

Po zepsuciu:
https://github.com/juliee5008/breach-checker/actions/runs/45888406297

Po poprawce:
https://github.com/juliee5008/breach-checker/actions/runs/45888960998

Wcześnie latest był publikowany przed testami dymnymi, więc mógł wskazywac na wadliwy obraz. Ma to znaczenie dla kogos, kto pobiera obraz bez podawania tagu, bo wtedy Docker autoamtycznie pobiera obraz z tagiem latest.

# 8.3

docker pull ghcr.io/juliee5008/breach-checker-backend:latest    

latest: Pulling from juliee5008/breach-checker-backend
04a82abfe4c5: Pull complete 
820e339d596c: Pull complete 
c2b12dac5cb1: Pull complete 
2edeb2f66a7e: Pull complete 
0c257c579742: Pull complete 
Digest: sha256:e2a2252a84be7f9416cb9a5276b24e7cabae84e02bc5c09c401eb874e0203323
Status: Downloaded newer image for ghcr.io/juliee5008/breach-checker-backend:latest
ghcr.io/juliee5008/breach-checker-backend:latest

docker pull ghcr.io/juliee5008/breach-checker-backend:latest@sha256:56270ce347bb62121bf14cf5ef75d65ebdfb8f0a9515d5d97c99ced414123f64

ghcr.io/juliee5008/breach-checker-backend@sha256:56270ce347bb62121bf08/breach-checker-backend
Digest: sha256:56270ce347bb62121bf14cf5ef75d65ebdfb8f0a9515d5d97c99ced414123f64
Status: Downloaded newer image for ghcr.io/juliee5008/breach-checker-backend@sha256:56270ce347bb62121bf14cf5ef75d65ebdfb8f0a9515d5d97c99ced414123f64
ghcr.io/juliee5008/breach-checker-backend:latest@sha256:56270ce347bb62121bf14cf5ef75d65ebdfb8f0a9515d5d97c99ced414123f64

docker images --digests ghcr.io/juliee5008/breach-checker-backend    

REPOSITORY                                  TAG       DIGEST                                                                    IMAGE ID       CREATED          SIZE
ghcr.io/juliee5008/breach-checker-backend   <none>    sha256:56270ce347bb62121bf14cf5ef75d65ebdfb8f0a9515d5d97c99ced414123f64   56270ce347bb   19 minutes ago   182MB
ghcr.io/juliee5008/breach-checker-backend   latest    sha256:e2a2252a84be7f9416cb9a5276b24e7cabae84e02bc5c09c401eb874e0203323   e2a2252a84be   19 minutes ago   182MB


docker push ghcr.io/juliee5008/breach-checker-backend:latest    

The push refers to repository [ghcr.io/juliee5008/breach-checker-backend]
286d8c291daa: Layer already exists 
83a14706aa6d: Layer already exists 
30cf67d7101c: Layer already exists 
e3e428093f5e: Layer already exists 
c2b12dac5cb1: Layer already exists 
820e339d596c: Layer already exists 
2edeb2f66a7e: Layer already exists 
0c257c579742: Layer already exists 
04a82abfe4c5: Layer already exists 
latest: digest: sha256:e2a2252a84be7f9416cb9a5276b24e7cabae84e02bc5c09c401eb874e0203323 size: 403

W --digests widac dwa podobne wpisy o różnych digestach
Docker pull działa, poneiwaz domyslnie publiczne repozytorium jest publiczne do odczytu. Docker push wymaga opdowiednich uprawnień
Token z write:packages służył przyznaniu uzytkownikowi tokenu dostepu do zapisu
