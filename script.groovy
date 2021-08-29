def buildApp() {
    sh """
    touch ola.txt
    echo Build for ${params.CUSTOMER}
    scp -i ola.txt $SSH_KEY:
    """
}

def testApp() {
    echo 'testing'
}

def deployApp() {
    echo 'testing'
}

return this
