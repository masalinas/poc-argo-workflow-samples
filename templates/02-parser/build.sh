# compile images and publish
docker build -t masalinasgancedo/poc-parser .

# run a docker from image
docker run masalinasgancedo/poc-parser

# puslish images on docker hub
docker push masalinasgancedo/poc-parser
