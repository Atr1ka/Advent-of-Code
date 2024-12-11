const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");

function part1() {
    let visible = {};
    for (let i=0; i<input.length; i++) {
        let shortest = -1;
        for (let j=0; j<input[i].length; j++) {
            if (input[i][j]>shortest) {
                visible[`${i},${j}`] = true;
                shortest = input[i][j];
            }
        }
    }
    for (let i=0; i<input.length; i++) {
        let shortest = -1;
        for (let j=input[i].length-1; j>-1; j--) {
            if (input[i][j]>shortest) {
                visible[`${i},${j}`] = true;
                shortest = input[i][j];
            }
        }
    }
    for (let j=0; j<input[0].length; j++) {
        let shortest = -1;
        for (let i=0; i<input.length; i++) {
            if (input[i][j]>shortest) {
                visible[`${i},${j}`] = true;
                shortest = input[i][j];
            }
        }
    }
    for (let j=0; j<input[0].length; j++) {
        let shortest = -1;
        for (let i=input.length-1; i>-1; i--) {
            if (input[i][j]>shortest) {
                visible[`${i},${j}`] = true;
                shortest = input[i][j];
            }
        }
    }
    return Object.keys(visible).length
}

function part2() {
    let  highest = 0;
    for (let i=0; i<input.length; i++) {
        for (let j=0; j<input[i].length; j++) {
            let a=0,b=0,c=0,d=0;
            // down
            for (let ix=i+1; ix<input.length; ix++) {
                a++;
                if (input[ix][j]>=input[i][j]) break;
            }
            // up
            for (let ix=i-1; ix>=0; ix--) {
                b++;
                if (input[ix][j]>=input[i][j]) break;
            }
            // right
            for (let jx=j+1; jx<input[0].length; jx++) {
                c++;
                if (input[i][jx]>=input[i][j]) break;
            }
            // left
            for (let jx=j-1; jx>=0; jx--) {
                d++;
                if (input[i][jx]>=input[i][j]) break;
            }
            highest = Math.max(highest, a*b*c*d);
        }
    }
    return highest;
}

console.log(part1())