pipeline {
environment {  
registry = "paulmercer/flaskapp"  
registryCredential = 'dockerhub_id'
dockerImage = ''
}
agent any
stages {
stage ('Install requirements')
{
    steps{
        script {
            sh 'pip install -r requirements.txt'
        }
    }
}
stage ('Running tests'){
    steps{
        script {
            sh 'pytest'
        }
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
