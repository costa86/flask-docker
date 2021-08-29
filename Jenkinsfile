pipeline {
    agent any

    stages {
        stage('First') {
            environment {
                SSH_KEY = credentials('COSTA_PRIVATE_KEY')
            }
            steps {
                git credentialsId: 'GITHUB_CREDENTIALS', url: 'https://github.com/costa86/flask-docker'
                echo 'Hello World'
                sh """
                ls
                pwd
                whoami
                touch lou.txt
                echo "Running ${env.GIT_URL}"
                """
            }
        }
    }
}
