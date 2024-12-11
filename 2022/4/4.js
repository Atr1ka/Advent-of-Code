const fs = require("fs");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");
function part1() {
    let sum = 0;
    for (e of input) {
        e = e.split(",");
        let a = e[0].split("-"), b = e[1].split("-");
        a[0]  = parseInt(a[0])
        a[1]  = parseInt(a[1])
        b[0]  = parseInt(b[0])
        b[1]  = parseInt(b[1])

        if ((a[0]<=b[0] && a[1]>=b[1]) || (b[0]<=a[0] && b[1]>=a[1])) {
            sum++;
        }
    }
    return sum;
}
function part2() {
    let sum = 0;
    for (e of input) {
        e = e.split(",");
        let a = e[0].split("-"), b = e[1].split("-");
        a[0]  = parseInt(a[0])
        a[1]  = parseInt(a[1])
        b[0]  = parseInt(b[0])
        b[1]  = parseInt(b[1])

        if (!(a[0]>b[1] || a[1]<b[0]))
            sum++;
    }
    return sum;
}
console.log(part1())