pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello from Stage 1!'
            }
        }

        stage('Stage 2') {
            steps {
                echo 'Hello from Stage 2!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
