# compile images and publish
docker build -t masalinasgancedo/biometric-import .

# run a docker from image
docker run masalinasgancedo/biometric-import

# puslish images on docker hub
docker push masalinasgancedo/biometric-import
