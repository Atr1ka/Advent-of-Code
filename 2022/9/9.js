const fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("in.txt", "utf-8").toString().split("\r\n");

function part1() {
    let visited = {}, head = [0,0], tail = [0,0];
    visited[tail[0]+","+tail[1]] = true;
    for (let e of input) {
        e = e.split(" ");
		for (let i=0; i<e[1]; i++) {
			if (e[0]=="R") head[0]++;
            else if (e[0]=="L") head[0]--;
            else if (e[0]=="D") head[1]--;
            else if (e[0]=="U") head[1]++; 
            
            if (Math.abs(head[0]-tail[0])<2 && Math.abs(head[1]-tail[1])<2);
            else if (head[0]==tail[0]) 
                tail[1] += (head[1]>tail[1]+1?1:(head[1]<tail[1]-1?-1:0))
            else if (head[1]==tail[1]) 
                tail[0] += (head[0]>tail[0]+1?1:(head[0]<tail[0]-1?-1:0))
            else {
                tail[0] += (head[0]>tail[0]?1:(head[0]<tail[0]?-1:0))
                tail[1] += (head[1]>tail[1]?1:(head[1]<tail[1]?-1:0))
            }
            visited[tail[0]+","+tail[1]] = true;
		}
    }
    return Object.keys(visited).length
}

function part2() {
    let visited = {}, coords = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]];
    visited[coords[9][0]+","+coords[9][1]] = true;
    for (let e of input) {
        e = e.split(" ");
		for (let j=0; j<e[1]; j++) {
			if (e[0]=="R") coords[0][0]++;
            else if (e[0]=="L") coords[0][0]--;
            else if (e[0]=="D") coords[0][1]--;
            else if (e[0]=="U") coords[0][1]++; 
            for (let i=0; i<9; i++) {
                if (Math.abs(coords[i][0]-coords[i+1][0])<2 && Math.abs(coords[i][1]-coords[i+1][1])<2);
                else if (coords[i][0]==coords[i+1][0]) 
                    coords[i+1][1] += (coords[i][1]>coords[i+1][1]+1?1:(coords[i][1]<coords[i+1][1]-1?-1:0))
                else if (coords[i][1]==coords[i+1][1]) 
                    coords[i+1][0] += (coords[i][0]>coords[i+1][0]+1?1:(coords[i][0]<coords[i+1][0]-1?-1:0))
                else {
                    coords[i+1][0] += (coords[i][0]>coords[i+1][0]?1:(coords[i][0]<coords[i+1][0]?-1:0))
                    coords[i+1][1] += (coords[i][1]>coords[i+1][1]?1:(coords[i][1]<coords[i+1][1]?-1:0))
                }
            }
            visited[coords[9][0]+","+coords[9][1]] = true;
		}
    }
    return Object.keys(visited).length
}

console.log(part1())