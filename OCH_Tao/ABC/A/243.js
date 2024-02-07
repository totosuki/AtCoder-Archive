let [V, A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const L = [A, B, C];
for (let i = 0; i < 1e5 + 1; i++) {
  V -= L[i % 3];
  if (V < 0) {
    if (i % 3 === 0) {
      console.log("F");
      break;
    } else if (i % 3 === 1) {
      console.log("M");
      break;
    } else {
      console.log("T");
      break;
    }
  }
}