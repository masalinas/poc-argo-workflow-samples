# compile images and publish
docker build -t masalinasgancedo/poc-volume-import .

# run a docker from image
docker run masalinasgancedo/poc-volume-import

# puslish images on docker hub
docker push masalinasgancedo/poc-volume-import
