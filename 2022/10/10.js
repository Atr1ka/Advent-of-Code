const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");

function part1() {
    let cycle = 0, line=0, x=1, next=0, interesting = [20,60,100,140,180,220], sum=0;
    while (++cycle && line<input.length) {
        if (interesting.includes(cycle))   
            sum+=x*cycle;
        if (next) {
            x+=next;
            next=0;
        }
        else {
            if (input[line].split(" ")[0]=="addx")
                next = parseInt(input[line].split(" ")[1]);
            line++;
        }
    }
    return sum;
}

function part2() {
    let cycle = 0, line=0,x=1, next=0;
    while (++cycle && line<input.length) {
        process.stdout.write((Math.abs(cycle-1-x)<2)?"#":".");
        if (cycle==40) {
            cycle-=40
            process.stdout.write("\n");
        }
        if (next) {
            x+=next;
            next=0;
        }
        else {
            if (input[line].split(" ")[0]=="addx")
                next = parseInt(input[line].split(" ")[1]);
            line++;
        }
    }
    return;
}

console.log(part1())