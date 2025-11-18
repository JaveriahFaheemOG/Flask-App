pipeline {

    agent any

    // Global environment variables
    environment {
        VERSION = "1.0"
    }

    // Tools (Make sure Maven name matches Jenkins → Manage Jenkins → Tools)
    tools {
        maven 'Maven3'
    }

    // Build parameters
    parameters {
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run Test Stage?')
    }

    stages {

        stage('Build') {
            steps {
                echo "Building version ${VERSION}"

                // Check Maven installation
                // Use "bat" instead of "sh" if you are on Windows
                sh "mvn --version"
            }
        }

        stage('Test') {
            when {
                expression { params.executeTests == true }
            }
            steps {
                echo "Running tests for version ${VERSION}"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying version ${VERSION}"
            }
        }
    }

    post {
        always {
            echo "Post-build actions executed."
        }
    }
}
