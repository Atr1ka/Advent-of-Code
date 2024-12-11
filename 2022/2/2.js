const fs = require("fs");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\n");
function part1() {
    let totalScore = 0;
    for (let e of input) {
        let a = e[0].charCodeAt(0)-'A'.charCodeAt(0), b = e[2].charCodeAt(0)-"X".charCodeAt(0);
        totalScore += b+1;
        if (a==b) totalScore += 3;
        if ((a+1)%3==b) totalScore += 6;
    }
    return totalScore;
}
function part2() {
    let totalScore = 0;
    for (let e of input) {
        let a = e[0].charCodeAt(0)-'A'.charCodeAt(0);
        let b = e[2].charCodeAt(0)-"X".charCodeAt(0);
        totalScore += b*3;
        console.log(totalScore)
        if (b==0) {
            totalScore += ((a+2)%3) + 1;
        }
        else if (b==1)
                totalScore += a+1
        else 
                totalScore += ((a+1)%3) + 1
        // console.log(totalScore)
    }
    return totalScore;
}
console.log(part2())