f1=function(v1){
	console.log('this is f1-',v1);
}
f2=function(v1){
	console.log('this is f2-',v1);
}

x=[f1,f2]

x.forEach(function(item){
	item('abcd');
});
