node {
   stage 'Checkout'
   checkout scm

   stage 'Build'
   // Run the maven build
   echo "this is test branch"

   stage 'check result'
   sh 'touch /tmp/test1&&ls /tmp/test1'
}

}
