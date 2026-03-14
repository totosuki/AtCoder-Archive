use proconio::input;
use proconio::marker::Chars;

fn main() {
    input!{
        N: usize,
        L: usize,
        R: usize,
        S: Chars,
    }

    let mut cnt = 0i64;
    let a = 'a' as usize;
    let mut  data = vec![vec![0; 26]; N];

    

    for i in 0..N {
        let s = S[i] as usize;

        if i+L < N {
            data[i+L][s-a] += 1;
        }

        if i+R+1 < N {
            data[i+R+1][s-a] -= 1;
        }
    }

    for i in 1..N {
        for j in 0..26 {
            data[i][j] += data[i-1][j]
        }
    }

    for i in 0..N {
        let s = S[i] as usize;
        cnt += data[i][s-a];
    }

    println!("{}", cnt);
}
