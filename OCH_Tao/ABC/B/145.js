const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
if (parseInt(N, 10) % 2 !== 0) {
  console.log("No");
} else {
  if (S.slice(0, parseInt(N, 10) / 2) === S.slice(parseInt(N, 10) / 2)) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}