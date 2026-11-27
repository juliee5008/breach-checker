# 9.1

# HELP log_attempts_total Licznik prób logowania
# TYPE log_attempts_total counter
log_attempts_total{found="true"} 10.0
log_attempts_total{found="false"} 4.0

Po jeszcze kilku probach logowania w grafanie mozna odczytac 12 prób dla found=false i 7 dla found=true

Etykieta found ze względu na bezpieczeństwo i szeregi czasowe Prometheusa; dluzsze teksty powoduja zuzycie procesora i pamięci przez kontener
Licznik po docker compose up -d --build log nie restartuje się tzn. zachowuje swoja wartość, ponieważ prometheus pobral juz wczesniej te wartosci i przechowuje je