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
            environment {
                CONTAINER_ID=$(docker ps -alq)
            }
            
            steps {
                sh '''
                cd ./cidr_convert_api/python/
                pip freeze > requirements.txt
                echo $CONTAINER_ID
                docker build -t dkvs
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