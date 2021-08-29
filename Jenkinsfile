pipeline {
    agent any
    stages {
        stage('Git') {
            steps {
                sh """
                ls
                pwd
                whoami
                echo "Commit $GIT_COMMIT"
                echo "Branch $GIT_BRANCH"
                """
            }
        }
    }
    post {
        always {
            mail to: 'costa86@zoho.com',
             subject: "Failed Pipeline",
             body: "Something is wrong with BUILD_URL"
        }
    }
}
