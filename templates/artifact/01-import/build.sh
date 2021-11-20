# compile images and publish
docker build -t masalinasgancedo/poc-artifact-import .

# run a docker from image
docker run masalinasgancedo/poc-artifact-import

# puslish images on docker hub
docker push masalinasgancedo/poc-artifact-import
