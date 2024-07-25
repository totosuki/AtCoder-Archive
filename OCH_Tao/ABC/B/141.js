const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
for (let i = 0; i < S.length; i++) {
  if (i % 2 === 0) {
    if (S[i] === "L") {
      console.log("No");
      break;
    }
  } else {
    if (S[i] === "R") {
      console.log("No");
      break;
    }
  }
  if (i === S.length - 1) {
    console.log("Yes");
  }
}