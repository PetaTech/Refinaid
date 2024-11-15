# build the docker image and run the container
docker-compose up -d

# follow the logs
docker-compose logs -f

# stop the container but keep the container
docker-compose stop

# stop the container and discard the container
docker-compose down
