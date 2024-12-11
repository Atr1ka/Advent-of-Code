const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");
function part1() {
    let sum = 0;
    for (e of input) {
        let a = e.substr(0, e.length/2), b = e.substr(e.length/2);
        // console.log(a + " " + b)
        for (i=0;i<a.length;i++) {
            if (b.includes(a[i])) {
                sum+= a[i].toUpperCase()===a[i] ? a[i].charCodeAt(0)-"A".charCodeAt(0)+27 : a[i].charCodeAt(0)-"a".charCodeAt(0)+1;
                break;
            }
        }
    }
    return sum;
}
function part2() {
    let sum = 0;
    for (let j=0;j<input.length;j+=3) {
        let a = input[j], b = input[j+1], c = input[j+2];
        for (i=0;i<a.length;i++) {
            if (b.includes(a[i]) && c.includes(a[i])) {
                sum+= a[i].toUpperCase()===a[i] ? a[i].charCodeAt(0)-"A".charCodeAt(0)+27 : a[i].charCodeAt(0)-"a".charCodeAt(0)+1;
                break;
            }
        }
    }
    return sum;
}
console.log(part1())