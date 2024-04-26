const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1]];
let cnt = { "T": 0, "A": 0 };
S.forEach(i => cnt[i] = (cnt[i] || 0) + 1);
if (cnt["T"] > cnt["A"]) {
  console.log("T");
} else if (cnt["T"] < cnt["A"]) {
  console.log("A");
} else {
  if (S.lastIndexOf("T") < S.lastIndexOf("A")) {
    console.log("T");
  } else {
    console.log("A");
  }
}