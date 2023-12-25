const ABC = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let l = [];
l.push(ABC[0] + ABC[1]);
l.push(ABC[1] + ABC[2]);
l.push(ABC[2] + ABC[0]);
l.sort((a, b) => a - b);
console.log(l[0]);