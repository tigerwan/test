node {
   stage 'Checkout'
   checkout scm

   stage 'Build'
   // Run the maven build
   echo "this is master branch"
   
   stage 'check result'
   sh 'touch /tmp/master&&ls /tmp/master'
}
