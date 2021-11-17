# compile images and publish
docker build -t masalinasgancedo/biometric-persist .

# run a docker from image
docker run masalinasgancedo/biometric-persist

# puslish images on docker hub
docker push masalinasgancedo/biometric-persist
