#!/bin/bash
set -e
# caminho onde colocamos o repo no server
WORKDIR=/srv/tcc-epi-federated
if [ ! -d "$WORKDIR" ]; then
  git clone https://github.com/YOUR_GITHUB_USER/YOUR_REPO.git $WORKDIR
else
  cd $WORKDIR
  git pull
fi
cd $WORKDIR/server
docker-compose pull || true
docker-compose up -d --build
