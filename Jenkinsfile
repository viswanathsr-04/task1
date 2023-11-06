pipeline {
  agents any
  triggers {
    gitHubPush()
  }
stages {
  stage("checkout") {
    steps {
      checkout scm
    }
  }
}
}
