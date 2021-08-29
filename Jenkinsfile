pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '', description: 'Software version')
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
        stage('Tests') {
            when {
                expression {
                    params.RUN_TESTS
                }
            }
            steps {
                sh '''
                echo "Testing the app"
                '''
            }
        }
        stage('Example') {
        input {
            message 'Should we continue?'
            ok 'Yes, we should.'
            submitter 'alice,bob'
            parameters {
                string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
            }
        }
        steps {
            echo "Hello, ${PERSON}, nice to meet you."
        }
        }
    }
}
