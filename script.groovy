def buildApp() {
    sh """
    touch ola.txt
    echo Build for ${params.CUSTOMER}
    """
}

def testApp() {
    echo 'testing'
}

def deployApp() {
    echo 'testing'
}

return this
