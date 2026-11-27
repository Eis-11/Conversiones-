pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Descarga') {
            steps {
                git url: 'https://github.com/Eis-11/Conversiones-.git', branch: 'main'
            }
        }

        stage('Instalacion') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Prueba') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    python -m pytest -v --junitxml=reports/resultados.xml
                '''
            }
            post {
                always {
                    junit 'reports/resultados.xml'
                }
            }
        }

        stage('Empaquetado') {
            steps {
                archiveArtifacts artifacts: '*.py', fingerprint: true
            }
        }
    }
}
