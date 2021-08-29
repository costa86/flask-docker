pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: "", description: 'Software version')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Should tests be executed?')
        choice(name: 'CUSTOMER', choices: ['One', 'Two', 'Three'], description: 'Customer to build to')
    }
    stages {
        stage('Start') {
            steps {
                sh """
                echo "Hello ${params.VERSION}"
                echo "Hello ${params.RUN_TESTS}"
                echo "Hello ${params.CUSTOMER}"
                """
            }
        }
    }
}
