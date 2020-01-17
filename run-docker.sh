# Navigate to the build directory
cd /home/mmanopoli/Udemy/RestAPIsWithFlaskAndPython/9__Deploying_Flask_apps_to_our_own_server__DOCKER

# Setup the fullstack network with driver bridge
docker network create fullstack -d bridge

# Use the docker-compose.yml and Dockerfile files to rebuild the images and stand up all 4 servers
docker-compose up --build

# For taking the whole thing down
docker-compose down -v;docker image prune;docker volume prune