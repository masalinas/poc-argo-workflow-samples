# compile images and publish
docker build -t masalinasgancedo/biometric-parser .

# run a docker from image
docker run masalinasgancedo/biometric-parser

# puslish images on docker hub
docker push masalinasgancedo/biometric-parser
