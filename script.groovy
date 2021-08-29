def buildApp() {
    sh """
    touch ola.txt
    echo Build for ${params.CUSTOMER}
    sh 'scp -i $SSH_KEY ola.txt costa@142.93.100.139:'
    """
}

def testApp() {
    echo 'testing'
}

def deployApp() {
    echo 'testing'
}

return this
