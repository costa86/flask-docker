def buildApp() {
    sh 'touch show.txt'
    sh 'scp -i $SSH_KEY show.txt costa@142.93.100.139:'
}

def testApp() {
    echo 'testing'
}

def deployApp() {
    echo 'testing'
}

return this
