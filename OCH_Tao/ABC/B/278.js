let [H, M] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
while (true) {
  const A = Math.floor(H / 10);
  const B = H % 10;
  const C = Math.floor(M / 10);
  const D = M % 10;
  if (A * 10 + C < 24 && B * 10 + D < 60) {
    console.log(H, M);
    break;
  } else {
    M++;
    if (M === 60) {
      M = 0;
      H++;
      if (H === 24) {
        H = 0;
      }
    }
  }
}