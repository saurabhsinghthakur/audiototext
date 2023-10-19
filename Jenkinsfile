pipeline {
    agent any

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    // Use the Docker image with Docker Compose installed
                    docker.image('docker/compose:1.29.2').inside('-u root') {
                        // Set up Docker Compose inside the Jenkins agent
                        sh 'docker-compose --version'
                        sh 'docker-compose build'
                        sh 'docker-compose up -d'
                    }
                }
            }
        }
    }
}
