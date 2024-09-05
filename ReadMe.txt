
EC2 Docker Deployment for Watermark Image Remover Application


:Steps to Deploy

1 Launch EC2 Instance

2 Connect to Instance

3  Install Docker

   ##if the user is root then u can skip sudo 

sudo apt update

: to install docker on ubuntu

sudo apt install -y docker.io

sudo systemctl start docker

sudo systemctl enable docker


4 repo cloning in ec2

git clone https://github.com/Urpritesh22/Watermark_Image_remover_flask.git


5 Build the Docker Image

to build the Docker image using the provided Dockerfile in the repo::

sudo docker build -t flask-app .


6. creating container::

sudo docker run -d -p 5000:5000 flask-app


7 copy public ip of ur ec2 and add port number 5000 as following format::

http://<your-ec2-public-ip>:5000

for accessing the app in web browser
