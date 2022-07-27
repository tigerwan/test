new File("/tmp/abc").eachFile() {
      file ->
      //if file.getName().endsWith(".txt") {
         println file.getName()
	//}
}
