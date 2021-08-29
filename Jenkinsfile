def gv

pipeline {
    agent any
    environment {
        SSH_KEY = credentials('PRIVATE_KEY')
    }
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
                script {
                    gv = load 'script.groovy'
                }
            }
        }
        stage('Tests') {
            when {
                expression {
                    params.RUN_TESTS
                }
            }
            steps {
                script {
                    gv.testApp()
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    gv.buildApp()
                }
            }
        }
        stage('Final') {
            steps {
                script {
                    def browsers = ['chrome', 'firefox']
                    def map = [name: "Jerry", age: 42, city: "New York"]
                    echo "${map.name}"
                    for (int i = 0; i < browsers.size(); ++i) {
                        echo "Testing the ${browsers[i]} browser"
                    }
                }
            }
        }
    }
}
