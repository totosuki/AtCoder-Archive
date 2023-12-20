const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
let x = [];
for (let i = 0; i < input.length; i++) {
  if (!x.includes(input[i])) {
    x.push(input[i]);
  }
}
console.log(x.length);