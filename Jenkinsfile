pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'priteshchopade22/image-watermark-project'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    // Stop the container if it's already running
                    sh 'docker ps -q -f "ancestor=$DOCKER_IMAGE" | xargs -r docker stop'
                    // Remove the container if it exists
                    sh 'docker ps -aq -f "ancestor=$DOCKER_IMAGE" | xargs -r docker rm'
                    // Run the Docker container
                    sh "docker run -d -p 5000:5000 $DOCKER_IMAGE"
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful! Access your application at http://<your-ec2-public-ip>:5000'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
