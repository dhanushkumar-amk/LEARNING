
type User = {
    id : string;
    name : string;
    email? : string; // ? indicates that this property is optional it is equal to email : string | undefined
    readonly createdAt : Date | null; // readonly indicates that this property cannot be modified after initialization
}

const user1 : User = {
    id : "1",
    name : "John",
    email : "user@gmail.com",
    createdAt : new Date()
}
// user1.createdAt = new Date() // Error: Cannot assign to 'createdAt' because it is a read-only property.
// user1.email = "XXXXXXXXXXXXXXX" => OK
// user1.createdAt = null =>  OK beacause null is allowed

const user2 : User = {
    id : "2",
    name : "Jane",
    createdAt : null
}

type User1 = { email ?: string }
type User2 = { email : string | undefined }

type Count = { [key : string] : number }
// index signature: it indicates that the object can have any number of properties with string keys and number values
const count = {
    apples : 10,
    oranges : 20,
    bananas : 15
}


// record utility type means we can create an object type with a specific set of keys and values of a specific type here the keys are "views", "likes", "dislikes" and the values are of type number
type Video = Record< "views" | "likes" | "dislikes", number | string >
const video : Video = {
    views : 1000,
    likes : 100,
    dislikes : 10
}
