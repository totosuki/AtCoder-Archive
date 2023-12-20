const C = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const L = ["a", "i", "u", "e", "o"];
if (L.includes(C)) {
  console.log("vowel");
} else {
  console.log("consonant");
}