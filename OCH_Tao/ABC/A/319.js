const D = { "tourist": 3858, "ksun48": 3679, "Benq": 3658, "Um_nik": 3648, "apiad": 3638, "Stonefeang": 3630, "ecnerwala": 3613, "mnbvmar": 3555, "newbiedmy": 3516, "semiexp": 3481 };
const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(D[S]);