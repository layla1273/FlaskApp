pipeline {
environment {  
registry = "paulmercer/flaskapp"  
registryCredential = 'dockerhub_id'
dockerImage = ''
}
agent any
    stages {
    stage('Building our image') {
    steps{
    script {
    dockerImage = docker.build registry + ":$BUILD_NUMBER"
    }
    }
    }

    stage('Demo stage 1'){
        steps{
            scripts{
                sh 'uname -a'
            }
        }
    }

    stage('Demo stage 2'){
        agent {
            docker 'python:3.6-alpine'
        }
        steps{
            scripts{
                sh 'uname -a'
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
