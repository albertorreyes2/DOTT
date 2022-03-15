pipeline {
    agent any
    environment {
        SCANNER_HOME= tool 'sonarDOTT'
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                echo "${SCANNER_HOME}"
                '''
                withSonarQubeEnv('SonarCloud') {
                sh 'cd ./cidr_convert_api/python/'
                sh '${SCANNER_HOME}/bin/sonar-scanner'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}