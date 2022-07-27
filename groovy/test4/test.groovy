
import groovy.io.FileType
def  accountList = []
def  envList = []
/*
new File("/Users/wand/Work/github/nct-lz-aws-toolIAM/accounts/nau").eachDir()
{
    dirs -> dirs.getName()
    if ( !dirs.getName().startsWith('bu_roles') ) {
        if ( !dirs.getName().startsWith('.') ) {
            //println "dir:${dirs.getName()}"
            new File("/Users/wand/Work/github/nct-lz-aws-toolIAM/accounts/nau/${dirs.getName()}").eachFile()
            {
                File file ->
                if (file.getName().endsWith('.tfvars')) {
                    println("file path:${file.absolutePath}" )
                    file.withReader() {
                        reader ->
                        while ( (line = reader.readLine()) != null ) {
                            def matcher = line =~ /\s*env\s*=\s*"(\w+)"/
                            println "matcher: ${matcher}"
                            if ( matcher.size() > 0 ) {
                                envList.add(matcher[0][1])
                                break
                            }
                        }
                    }
                }
            }
        }
    }
}
*/
new File("/Users/wand/Work/github/nct-lz-aws-toolIAM/accounts/nau").eachDir()
{
    dirs ->
    def accountName = dirs.getName()
    if ( !accountName.startsWith('bu_roles') && !accountName.startsWith('.') ) {
        new File("/Users/wand/Work/github/nct-lz-aws-toolIAM/accounts/nau/${accountName}").eachFile()
        {
            File file ->
            if (file.getName().endsWith('.tfvars')) {
                file.withReader() {
                    reader ->
                    while ( (line = reader.readLine()) != null ) {
                        // search env=<environment> lines, and fetch <environment>
                        def matcher = line =~ /env\s*=\s*"(\w+)"/
                        println "matcher: ${matcher}"
                        if ( matcher != null && matcher.size() > 0 ) {
                            envList.add("all ${matcher[0][1]} accounts".toString())
                            break
                        }
                    }
                }
            }
        }
    }
}

println "envList: ${envList.unique().sort()}"