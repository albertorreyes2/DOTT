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
                withSonarQubeEnv('sonarDOTT') {
                sh 'cd ./cidr_convert_api/python/'
                sh '${SCANNER_HOME}/bin/sonar-scanner'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'U Testing..'
                sh ''' 
                python --version
                cd ./cidr_convert_api/python/
                pip install -r requirements.txt
                python tests.py 
                '''
            }
        }
        
        stage('Build img') {
            steps {
                sh '''
                cd ./cidr_convert_api/python/
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}