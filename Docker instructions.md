# To build a docker container 
docker build -t my-app .

# To run the container interactively with port assigned 8000
docker run -it -p 8000:8000 my-app