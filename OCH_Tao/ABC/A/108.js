const K = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (K % 2 === 0) {
  console.log((K / 2) ** 2);
} else {
  console.log((Math.ceil(K / 2)) * (Math.floor(K / 2)));
}