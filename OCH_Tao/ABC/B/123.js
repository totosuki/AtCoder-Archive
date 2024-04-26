const L = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let X = [];
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    if (i === j) {
      continue;
    }
    for (let k = 0; k < 5; k++) {
      if (i === k || j === k) {
        continue;
      }
      for (let l = 0; l < 5; l++) {
        if (i === l || j === l || k === l) {
          continue;
        }
        for (let m = 0; m < 5; m++) {
          if (i === m || j === m || k === m || l === m) {
            continue;
          }
          X.push([L[i], L[j], L[k], L[l], L[m]]);
        }
      }
    }
  }
}
let rslt = [];
for (const A of X) {
  let cnt = 0;
  for (let i = 0; i < 5; i++) {
    cnt += A[i];
    if (i === 4) {
      break;
    }
    while (cnt % 10 > 0) {
      cnt++;
    }
  }
  rslt.push(cnt);
}
console.log(Math.min(...rslt));