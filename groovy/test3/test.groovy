/*
import java.text.SimpleDateFormat
import groovy.io.FileType
if (fileExists("/tmp/testdir")) {
	println "got it"
}
else {
	println "not see it"
}
*/

z='z'
def x=[ 'x': ['a':'a','b':'b'], 'y':['1':'1','2':'2']]

x[z] = "aaaaaa"

println x.containsKey('z')
println x.x
println x.z

if (x["m"] != null && x["m"]["n"] != null) {
	println x.m.n
}
else
{
	println "no see it"
}
