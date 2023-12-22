const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
console.log((((input[0])[0]) + ((input[1])[0]) + ((input[2])[0])).toUpperCase());