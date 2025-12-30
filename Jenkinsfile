pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/JaveriahFaheemOG/Flask-App.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Application') {
            steps {
                sh 'mkdir -p build'
                sh 'cp -r . build/'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'mkdir -p /tmp/flask-deploy'
                sh 'cp -r build/* /tmp/flask-deploy/'
            }
        }
    }
}
