pipeline {
environment {  
registry = "paulmercer/flaskapp"  
registryCredential = 'dockerhub_id'
dockerImage = ''
HOME = "${env.WORKSPACE}"
}
agent any
    stages {
    stage ('Testing')
        {
            steps{
            sh 'pip install -r requirements.txt'
            sh 'pytest --junitxml results.xml'
            }
        }

    stage('Building our image') {
    steps{
    script {
    dockerImage = docker.build registry + ":$BUILD_NUMBER"
    }
    }
    }

    stage('Deploy our image') {
    steps{
    script {
    docker.withRegistry( '', registryCredential ) {
    dockerImage.push()
    }
    }
    }
    }
stage('Cleaning up') {
steps{
sh "docker rmi $registry:$BUILD_NUMBER"
}
}
}
}
