async function f(input){
	console.log('here is ', input);
 	return '123'	
}
async function master(){
	console.log('before callback');
	x=await f('abc')
	console.log('got callback ', x);
}
console.log('before master')
master()
console.log('after master')

