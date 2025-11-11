set -e
# repo no server
WORKDIR=/srv/tcc-epi-federated
if [ ! -d "$WORKDIR" ]; then
  git clone https://github.com/adrianamartani/epi-federated-learning-devsecops.git $WORKDIR
else
  cd $WORKDIR
  git pull
fi
cd $WORKDIR/server
docker-compose pull || true
docker-compose up -d --build
