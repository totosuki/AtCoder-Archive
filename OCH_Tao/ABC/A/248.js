const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
for (let i = 0; i < 10; i++) {
  if (!S.includes(String(i))) {
    console.log(i);
  }
}