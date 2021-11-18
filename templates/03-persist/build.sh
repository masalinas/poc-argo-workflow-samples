# compile images and publish
docker build -t masalinasgancedo/poc-persist .

# run a docker from image
docker run masalinasgancedo/poc-persist

# puslish images on docker hub
docker push masalinasgancedo/poc-persist