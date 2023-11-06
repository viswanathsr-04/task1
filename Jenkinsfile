pipeline {
  agent any
  triggers {
    gitHubPush()
  }
stages {
  stage('Checkout') {
    steps {
      checkout scm
    }
  }
}
}
