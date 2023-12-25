const ABC = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
if (ABC[0] === ABC[1]) {
  console.log(ABC[2]);
} else if (ABC[1] === ABC[2]) {
  console.log(ABC[0]);
} else {
  console.log(ABC[1]);
}