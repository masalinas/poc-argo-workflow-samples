# compile images and publish
docker build -t masalinasgancedo/poc-artifact-persist .

# run a docker from image
docker run masalinasgancedo/poc-artifact-persist

# puslish images on docker hub
docker push masalinasgancedo/poc-artifact-persist