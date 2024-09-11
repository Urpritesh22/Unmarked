Some PDFs contain watermarks embedded as background images, which can be difficult to remove manually. Typically, you would have to go through each page and remove the watermark image individually, which is time-consuming.

In this project, we developed an Image Watermark Remover Tool that automates this process. The tool has two functions:

Watermark Detection and Removal: It scans the PDF and automatically removes the background watermark image without affecting the main content, such as text or front images.
Image Verification: To ensure accuracy, it checks for watermarks by identifying images on a white background with gray text, making sure only the background image is removed.

//////////////////////////////////////////////////

EC2 Docker Deployment for Watermark Image Remover Application


:Steps to Deploy

1 Launch EC2 Instance

2 Connect to Instance

Modify Security group rules to allow for port 5000 or just open all traffic

3  Install Docker

   ##if the user is root then u can skip sudo 

sudo apt update

: to install docker on ubuntu

sudo apt install -y docker.io

sudo systemctl start docker

sudo systemctl enable docker

sudo usermod -aG docker $USER

newgrp docker


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
===================================================================================================================
-------------------------------------------------------------------------------------------------------------------
or you can directly install docker on your ec2 machine and create the container using the image from my Dockerhub repository.

Step 1: Login to Ec2 (Modify Security group settings for Port 5000): 

Step 2:  sudo apt update -y
         sudo apt install docker.io -y

Step 3: docker run -p 5000:5000 priteshchopade22/image-watermark-project

Step 4: http://<your-ec2-public-ip>:5000
