# compile images and publish
docker build -t masalinasgancedo/poc-artifact-parser .

# run a docker from image
docker run masalinasgancedo/poc-artifact-parser

# puslish images on docker hub
docker push masalinasgancedo/poc-artifact-parser
