const fs = require("fs");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");
console.log(input)
function part1() {
    let maxCalories = 0, c = 0;
    for (let e of input) {
        if (!e) {
            // console.log("test")
            maxCalories = Math.max(maxCalories, c);
            c = 0;
        }
        else {
            c += parseInt(e);
        }
    }
    return maxCalories
}
function part2() {
    let maxCalories = [], c = 0;
    for (let e of input) {
        if (!e) {
            maxCalories.push(c);
            c = 0;
        }
        else {
            c += parseInt(e);
        }
    }
    maxCalories.push(c);
    return maxCalories.sort((a, b) => b - a).slice(0, 3).reduce((a, c) => a + c)
}
console.log(part2())