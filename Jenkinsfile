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
                echo 'Unit testing'
                sh ''' 
                python --version
                cd ./cidr_convert_api/python/
                cat requirements.txt
                pip install -r requirements.txt
                python3 tests.py 
                '''                
            }
        }
        
        stage('Build img') {
            steps {
                sh '''
                cd ./cidr_convert_api/python/
                pwd
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