const fs = require("fs");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");
function part1() {
    let n = (input[0].length+1)/4, k, st = [], str="";
    for (let i=0;i<n;i++) st.push([]);
    for (let i=0; input[i+1]!==''; i++) {
        for (let j=1;j<input[i].length;j+=4)
            if (input[i][j]!==' ')
                st[(j-1)/4].unshift(input[i][j])
        k=i+2;
    }
    for (let i=k+1; i<input.length; i++) {
        input[i] = input[i].split(" ");
        let count = parseInt(input[i][1]);
        let a = parseInt(input[i][3])-1, b = parseInt(input[i][5])-1;
        for (let j=0; j<count; j++) {
            st[b].push(st[a].pop());
        }
    }
    for (let i=0;i<n;i++)
        str+=st[i].pop();
    return str;
}
function part2() {
    let n = (input[0].length+1)/4, k, st = [], str="";
    for (let i=0;i<n;i++) st.push([]);
    for (let i=0; input[i+1]!==''; i++) {
        for (let j=1;j<input[i].length;j+=4)
            if (input[i][j]!==' ')
                st[(j-1)/4].unshift(input[i][j])
        k=i+2;
    }
    for (let i=k+1; i<input.length; i++) {
        input[i] = input[i].split(" ");
        let count = parseInt(input[i][1]);
        let a = parseInt(input[i][3])-1, b = parseInt(input[i][5])-1;
        st[b].push(...st[a].slice(-count));
        st[a].length-=count;
    }
    for (let i=0;i<n;i++)
        str+=st[i].pop();
    return str;
}
console.log(part1())