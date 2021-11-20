# compile images and publish
docker build -t masalinasgancedo/poc-volume-parser .

# run a docker from image
docker run masalinasgancedo/poc-volume-parser

# puslish images on docker hub
docker push masalinasgancedo/poc-volume-parser
