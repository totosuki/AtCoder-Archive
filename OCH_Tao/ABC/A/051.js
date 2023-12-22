const s = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(",");
console.log(`${s[0]} ${s[1]} ${s[2]}`);