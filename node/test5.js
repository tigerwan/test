class BaseClass {
    constructor(){
        console.log('Object created INHERITED');
    }

    toCallFromChild(){
        console.log('Called by child');
        this.toOverride();
    }

    toOverride(){} //to override
}

class childClass extends BaseClass{
    toOverride(){
        console.log ('Override by child');
    }
}

var instance = new childClass();
instance.toCallFromChild();
