docker version

docker images

docker image rm ubuntu:18.04 --force

docker image rm hello-world --force

docker run hello-world

docker run -d hello-world

docker ps

# Container já apaga na hora

docker run --rm ubuntu:18.04 echo "teste"

# Mostrar que o container não fica em pé

docker run ubuntu:18.04 echo "teste"

docker run ubuntu:18.04 /bin/bash

docker run -it ubuntu:18.04 /bin/bash

# Quebrar um container de propósito, se eu tivesse em uma VM, e não tivesse backup, teria problemas

docker run -it ubuntu:18.04 /bin/bash

mv /bin /trash

# Docker inspect no container no ar

docker run -it ubuntu:18.04 /bin/bash

# outro terminal

docker ps

docker inspect

# Perder as coisas que fizemos no container

docker run -it --name cowsay ubuntu bash
apt-get update
apt-get install -y cowsay

/usr/games/cowsay "olá, alunos!"

docker exec -it cowsay bash


# Store image

docker run -it --name cowsay --hostname cowsay ubuntu bash
apt-get update
apt-get install -y cowsay

/usr/games/cowsay "olá, alunos!"

docker commit cowsay test/cowsayimage

docker run test/cowsayimage /usr/games/cowsay "Moo"

# demo dockerfile
# demo-Dockerfile-cowsay

docker run test/cowsay-dockerfile /usr/games/cowsay "agora dentro do container!"


# Redis com link

docker network create mynetwork

docker run --network=mynetwork --name myredis -d redis

docker run --rm -it --network=mynetwork redis /bin/bash


redis-cli -h myredis -p 6379

redis:6379> ping
PONG
redis:6379> set "abc" 123
OK
redis:6379> get "abc"
"123"


# PG network

docker network create pgnetwork
docker run -d --name postgres-db --network pgnetwork -e POSTGRES_PASSWORD=123456 postgres
docker run -d --name pgadmin --network pgnetwork -p 80:80 -e PGADMIN_DEFAULT_EMAIL=test@test.com -e PGADMIN_DEFAULT_PASSWORD=123456 dpage/pgadmin4
