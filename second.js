//salam to kaisay hain ap log kia hal hain
// console.log("hello world!");

//operators in javascript; perform some operations in javas.
//zrithmetic operators:

// let a = 2;
// let b = 7;
// console.log("a + b =" , a+ b);
// console.log("a / b =" , a/ b);
// console.log("a % b =" , a% b);
// console.log("a ** b =" , a** b); //2^7

// let a =3;
// let b = 4;
// console.log("a=" , a);
// ++a;
// console.log(a);


//assignment operators:
// let a = 6;
// let b = 4;

// a **= 12;
// console.log("a=" , a);

//comparison operator:
// let a = 3;
// let b = 4;
// console.log("3==4" , a==b);

// let c = 3;
// let d = 3;
// console.log("3!=3" , c!=d);


// for(let i = 1; i<=500; i++) {
//     console.log("habiba");
// }

// for(let a = 1; a<=700; a++){
//     console.log("BMW");
// }
// console.log("loop has ended");
// console.log("will buy BMW inshaAllah");

// let i = 1;
// while(i<=6);{
//     console.log("i");
//     i++;
// }

// let a = 1;
// do{
//     console.log("a=" , a);
//     a++;
// }
// while(a <= 5);

//for of loop:

// let str = "python javascript css html";
// let size =0

//  for( let i of str) {
//     console.log("i=", i);
//     size++;
//  }
// console.log("string size", size);

// for( let i = 0; i<=100; i++){
//     if(i%2!=0)
//     console.log(i);
// }


//  let str = ("rahmat ali");
//  console.log(str.length);

// let specialstring = 'this is a template literal ${1 + 2 + 3 }' ;
// console.log("specialstring");

// let str= ("habiba\trahmat ali");
// console.log(str.slice(1,3));

let fullname = prompt("enter your fullname without spaces");
let username = "@" + fullname + fullname.length;
console.log(username);
