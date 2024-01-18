const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (A === "a") {
  console.log(-1);
} else if (A.length === 1) {
  const X = A.charCodeAt(0);
  console.log(String.fromCharCode(X - 1));
} else {
  console.log(A.slice(0, A.length - 1));
}