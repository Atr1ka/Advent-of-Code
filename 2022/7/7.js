const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");

function part1() {
    let sum = 0;
    for (let i = 0; i < input.length; i++)
        if (/\$ ls/.test(input[i]))
            sum += dirSize1(i + 1);
    return sum;
}

function dirSize1(n) {
    let open = 1, sum = 0;
    while (open && sum <= 100000 && n < input.length) {
        // console.log(n, " ", open, " ", sum, " ", input[n]);
        if (/\d/.test(input[n][0]))
            sum += parseInt(input[n].split(" ")[0]);
        else if (/\$ cd \.\./.test(input[n]))
            open--;
        else if (/\$ cd /.test(input[n]))
            open++;
        n++;
    }
    return (sum > 100000) ? 0 : sum;
}

function part2() {
    let requiredSpace = dirSize2(2) - 40000000, closest = 70000000;
    for (let i = 2; i < input.length; i++)
        if (/\$ ls/.test(input[i])) {
            let size = dirSize2(i);
            if (size>requiredSpace)
                closest = Math.min(closest, size)
        }
    return closest;
}

function dirSize2(n) {
    let open = 1, sum = 0;
    while (open && n < input.length) {
        if (/\d/.test(input[n][0]))
            sum += parseInt(input[n].split(" ")[0]);
        else if (/\$ cd \.\./.test(input[n]))
            open--;
        else if (/\$ cd /.test(input[n]))
            open++;
        n++;
    }
    return sum;
}

console.log(part1())