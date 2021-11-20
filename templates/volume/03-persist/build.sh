# compile images and publish
docker build -t masalinasgancedo/poc-volume-persist .

# run a docker from image
docker run masalinasgancedo/poc-volume-persist

# puslish images on docker hub
docker push masalinasgancedo/poc-volume-persist