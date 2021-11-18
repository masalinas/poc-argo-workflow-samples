# compile images and publish
docker build -t masalinasgancedo/poc-import .

# run a docker from image
docker run masalinasgancedo/poc-import

# puslish images on docker hub
docker push masalinasgancedo/poc-import
