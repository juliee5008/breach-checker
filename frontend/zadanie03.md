# 1

PS C:\Users\lab04\jj_cyber\breach-checker> docker inspect --format '{{json .Config.Labels}}' julia-frontend:v1
{"autor":"Julia Jaros","data":"2026-10-16","maintainer":"julia.jaros"}
PS C:\Users\lab04\jj_cyber\breach-checker> docker inspect --format '{{json .Config.Labels}}' julia-frontend:latest
{"autor":"Julia Jaros","data":"2026-10-16","maintainer":"julia.jaros"}
PS C:\Users\lab04\jj_cyber\breach-checker> docker history julia-frontend:v1
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
25617d2c7f4d   4 minutes ago    EXPOSE [80/tcp]                                 0B        buildkit.dockerfile.v0
<missing>      4 minutes ago    RUN /bin/sh -c htmlhint /usr/share/nginx/htm…   4.1kB     buildkit.dockerfile.v0
<missing>      4 minutes ago    COPY . /usr/share/nginx/html # buildkit         32.8kB    buildkit.dockerfile.v0
<missing>      20 minutes ago   RUN /bin/sh -c apk add --no-cache nodejs npm…   102MB     buildkit.dockerfile.v0
<missing>      20 minutes ago   LABEL maintainer=julia.jaros autor=Julia Jar…   0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      RUN /bin/sh -c set -x     && apkArch="$(cat …   52.4MB    buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV ACME_VERSION=0.4.1                          0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV NJS_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV NJS_VERSION=1.0.1                           0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      COPY 30-tune-worker-processes.sh /docker-ent…   16.4kB    buildkit.dockerfile.v0
<missing>      3 weeks ago      COPY 20-envsubst-on-templates.sh /docker-ent…   12.3kB    buildkit.dockerfile.v0
<missing>      3 weeks ago      COPY 15-local-resolvers.envsh /docker-entryp…   12.3kB    buildkit.dockerfile.v0
<missing>      3 weeks ago      COPY 10-listen-on-ipv6-by-default.sh /docker…   12.3kB    buildkit.dockerfile.v0
<missing>      3 weeks ago      COPY docker-entrypoint.sh / # buildkit          8.19kB    buildkit.dockerfile.v0
<missing>      3 weeks ago      RUN /bin/sh -c set -x     && addgroup -g 101…   5.72MB    buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV DYNPKG_RELEASE=1                            0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV PKG_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENV NGINX_VERSION=1.31.6                        0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      4 weeks ago      CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      4 weeks ago      ADD alpine-minirootfs-3.24.2-x86_64.tar.gz /…   9.08MB    buildkit.dockerfile.v0

Tylko 5 górnych warstw pochodzi z mojego Dockerfile; pozostałe pochodzą z obrazu bazowego
nginx:alpine. Wpisy o wielkości 0B to instrukcje, które tylko dopisały metadane.
Ponieważ budujemy obraz bazujacy na nginx:alpine, ale nie będący mu równowaznym, to wartość
maintainer zostaje nadpisana z pliku tworzącego obraz (Dockerfile).

# 2

W obu kontenrach: Fri Oct 16 12:36:00 UTC 2026

PS C:\Users\lab04\jj_cyber\breach-checker> docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED              STATUS              PORTS                                     NAMES
a8a2796b1f16   julia-frontend:v2   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp   frontend2
4a7257be3faa   julia-frontend:v2   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   frontend1

Czas jest z momentu, w którym pierwszy raz uruchomiono polecenie RUN  date > /usr/share/nginx/html/build.txt
czyli podczas tworzenia obrazu

# 3

 root   /usr/share/nginx/html;

to folder którego pliki zostaja podmienione (jak wskazano w Dockerfile)

# 4
PS C:\Users\lab04\jj_cyber\breach-checker> docker exec frontend ls /usr/share/nginx
html
index.html
script.js
style.css
zadanie03.md
PS C:\Users\lab04\jj_cyber\breach-checker> docker exec frontend ls /usr/share/nginx/html
50x.html
build.txt
index.html

htmlhint sprawdził plik index.html z /usr/share/nginx/html który ma poprawną konstrukcje wiec
zaden blad nie został wykryty