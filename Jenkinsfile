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
}
