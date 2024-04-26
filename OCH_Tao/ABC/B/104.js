const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const re = /A[a-z]{1}[a-z]*C[a-z]*[a-z]{1}$/;
if (re.test(S)) {
  console.log("AC");
} else {
  console.log("WA");
}