const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
console.log(`A${(input[1])[0]}C`);