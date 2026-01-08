// let title : string = "TypeScript Special Types";
// title = undefined;


// union
let subTitle : string | undefined = "Learn TypeScript";
subTitle = undefined;
console.log(subTitle);


// void : function does't return anything
function logMessage() : void {
    console.log("This is a log message");
}

// never : function never returns
function throwError(message : string) : never {
    throw new Error(message);
}

// Don't use any try to avoid type checking
// any
let value: any = 10
value = "hello"
value = true
console.log(value);

// unknown
// The unknown type represents a value whose type is not known yet, but must be checked before use.
// It is the safe alternative to any.

let b : unknown = 20;
b = "TypeScript";
b = false;
console.log(b);

// Type assertion
// Type assertion tells TypeScript to treat a value as a specific type without runtime checks.
// It is a compile-time instruction only.

// as syntax
let c : unknown = "hello"
let str = c as string
console.log(str)


