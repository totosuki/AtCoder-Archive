const X = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"];
const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]
if (X.includes(S)) {
  console.log("Yes");
} else {
  console.log("No");
}