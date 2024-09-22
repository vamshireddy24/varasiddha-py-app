pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'  // Define virtual environment directory
        SONAR_URL = "http://localhost:9000"
        SONAR_PROJECT_KEY = "varasiddha-py-app"  // Define your SonarQube project key
        SONAR_SCANNER_HOME = '/home/ubuntu/sonar-scanner'
        DOCKER_IMAGE = "kubevamshi/varasiddha-py:${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
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
        stage('Run Tests and SonarQube Analysis') {
            parallel {
                stage('Run Tests') {
                    steps {
                        script {
                            // Run tests
                            sh '''
                            . ${VENV_DIR}/bin/activate
                            pytest tests --maxfail=1 --disable-warnings -q
                            '''
                        }
                    }
                }
                stage('SonarQube Analysis') {
                    steps {
                        script {
                            withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) {
                              //def scannerHome = tool 'SonarScanner'  // Ensure this matches the name in Global Tool Configuration
                                sh '''
                                . ${VENV_DIR}/bin/activate
                                ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                                -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                                -Dsonar.sources=/var/lib/jenkins/workspace/varasiddha-py-app/varasiddha \
                                -Dsonar.host.url=${SONAR_URL} \
                                -Dsonar.login=${SONAR_AUTH_TOKEN}
                                '''
                                // ${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=varasiddha-py-app -Dsonar.sources=. -Dsonar.host.url=${SONAR_URL} -Dsonar.login=${SONAR_AUTH_TOKEN}
                            }
                        }
                    }
                }
            }
        }
        stage('Build and Push Docker Image') {
            environment {
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
