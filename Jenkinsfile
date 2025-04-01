pipeline {
    agent any
    environment {
        EC2_PUBLIC_IP = credentials('ec2_public_ip')
    }
    stages {
        stage('GitHub Clone') {
            steps {
                git branch: 'main',
                    credentialsId: 'soundbar91',
                    url: 'https://github.com/Team-HLP/api-server'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['ssh_key']) {
                    sh '''
                        echo "📦 EC2로 프로젝트 복사 중..."
                        ssh -o StrictHostKeyChecking=no ubuntu@$EC2_PUBLIC_IP 'mkdir -p /home/ubuntu/app'
                        scp -r . ubuntu@$EC2_PUBLIC_IP:/home/ubuntu/app/

                        echo "🚀 EC2에서 Docker로 FastAPI 앱 실행 중..."
                        ssh -o StrictHostKeyChecking=no ubuntu@$EC2_PUBLIC_IP 'bash /home/ubuntu/config/deploy.sh'
                    '''
                }
            }
        }
    }
}
