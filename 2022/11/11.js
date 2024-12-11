const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");

function part1() {
    let N = (input.length+1)/7, m = [], ins = [];
    for (let i=0; i<N; i++) {
        ins.push(0)
		let monkey = {};
        monkey.vals = input[i*7+1].slice(18).split(", ").map(x=>parseInt(x));
        monkey.func = old => eval(input[i*7+2].slice(19));
        monkey.test = parseInt(input[(i*7)+3].split(" ")[5]);
        monkey.true = parseInt(input[(i*7)+4].split(" ")[9]);
        monkey.false = parseInt(input[(i*7)+5].split(" ")[9]);
        m.push(monkey);
    }
    for (let it=0; it<20; it++) {
        for (let i=0; i<m.length; i++) {
			while (m[i].vals.length) {
                ins[i]++;
                let val = m[i].vals.shift();
                val = m[i].func(val);
                val = Math.floor(val/3);
                m[(val%m[i].test==0 ? m[i].true : m[i].false)].vals.push(val);
            }
        } 
    }
    let max = ins.splice(ins.indexOf(ins.reduce((acc,e)=>Math.max(acc,e))), 1);
    return max * ins.reduce((acc,e)=>Math.max(acc,e));
}

function part2() {
    let N = (input.length+1)/7, m = [], ins = [], mod=1;
    for (let i=0; i<N; i++) {
        ins.push(0)
		let monkey = {};
        monkey.vals = input[i*7+1].slice(18).split(", ").map(x=>parseInt(x));
        monkey.func = old => eval(input[i*7+2].slice(19));
        monkey.test = parseInt(input[(i*7)+3].split(" ")[5]);
        if (mod%monkey.test) mod*=monkey.test;
        monkey.true = parseInt(input[(i*7)+4].split(" ")[9]);
        monkey.false = parseInt(input[(i*7)+5].split(" ")[9]);
        m.push(monkey);
    }
    for (let it=0; it<10000; it++) {
        for (let i=0; i<m.length; i++) {
			while (m[i].vals.length) {
                ins[i]++;
                let val = m[i].vals.shift();
                val = m[i].func(val);
                val %= mod;
                m[(val%m[i].test==0 ? m[i].true : m[i].false)].vals.push(val);
            }
        }
    }
    let max = ins.splice(ins.indexOf(ins.reduce((acc,e)=>Math.max(acc,e))), 1)[0];
    return max * ins.reduce((acc,e)=>Math.max(acc,e));
}

console.log(part1())