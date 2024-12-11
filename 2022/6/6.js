const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");
function part1() {
    input = input[0]
    for (i=4; i<input.length; i++) {
        if (input[i]!=input[i-1] && input[i]!=input[i-2] && input[i]!=input[i-3] && input[i]!=input[i-4] && input[i-1]!=input[i-2] && input[i-1]!=input[i-3] && input[i-1]!=input[i-4] && input[i-2]!=input[i-3] && input[i-2]!=input[i-4] && input[i-3]!=input[i-4])
            return i;
    }
}
function part2() {
    input = input[0]
    let prev = [];
    for (i=0; i<14; i++) prev.push(input[i]);
    for (i=14; i<input.length; i++) {
        console.log(prev.length + " " + new Set(prev).size)
        if (prev.length== new Set(prev).size) return i;
        prev.shift();
        prev.push(input[i]);
    }
    return -1;
}
console.log(part1())