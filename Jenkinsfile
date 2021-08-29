pipeline {
    agent any
    parameters {
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
    }
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
