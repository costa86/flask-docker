def buildApp() {
    sh 'scp -i $SSH_KEY hello.txt costa@142.93.100.139:'
}

def testApp() {
    echo 'testing'
}

def deployApp() {
    echo 'testing'
}

return this
