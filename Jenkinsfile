pipeline {
    agent any
     environment {
        VENV_DIR = 'venv'  // Define virtual environment directory
        SONAR_URL = "http://localhost:9000"
        SONAR_PROJECT_KEY = "varasiddha-py-app"  // Define your SonarQube project key
        DOCKER_IMAGE = "kubevamshi/varasiddha-py:${BUILD_NUMBER}"
    }
    stages {
        stage('checkout') {
            steps {
                sh 'echo passed'
                 git branch: 'main', url: "https://github.com/vamshireddy24/varasiddha-py-app.git"
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                // Install Python dependencies
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
      //  stage('Run Tests') {
      //      steps {
      //          script {
      //          // Run tests
      //              sh '''
      //              . ${VENV_DIR}/bin/activate
      //              pytest tests --maxfail=1 --disable-warnings -q
      //              '''
      //          }
      //      }
      //}
         stage('Sonar-Test') {
             environment {
                 SONAR_URL = "http://localhost:9000"
             }
            steps {
                script {
                    withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) {
                        // Run SonarQube Scanner
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        sonar-scanner \
                          -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=${SONAR_URL} \
                          -Dsonar.login=${SONAR_AUTH_TOKEN}
                          -Dsonar.projectKey=${SONAR_PROJECT_KEY}
                        '''
                    }
                }
            }
        }
        stage('Build and Push Docker Image') {
            environment {
                DOCKER_IMAGE = "kubevamshi/varasiddha-py:${BUILD_NUMBER}"
                REGISTRY_CREDENTIALS = credentials('docker-cred')
            }
            steps {
                script {
                    sh 'sudo docker build -t ${DOCKER_IMAGE} .'
                    def dockerImage = docker.image("${DOCKER_IMAGE}")
                    docker.withRegistry('https://index.docker.io/v1/', "docker-cred") {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
