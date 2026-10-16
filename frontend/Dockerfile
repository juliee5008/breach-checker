FROM nginx:alpine
LABEL maintainer="julia.jaros" autor="Julia Jaros" data="2026-10-16"
RUN apk add --no-cache nodejs npm && npm install -g htmlhint
COPY . /usr/share/nginx/html
RUN  date > /usr/share/nginx/html/build.txt
RUN htmlhint /usr/share/nginx/html/index.html
EXPOSE 80