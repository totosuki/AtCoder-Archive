use proconio::input;

fn main() {
    input! {
        H: i32,
        W: i32,
        Q: usize,
        queries: [[i32; 2]; Q],
    }

    let mut ny = H;
    let mut nx = W;

    queries.iter().for_each(|query| {
        let mut ans = 0;
        let qt = query[0];
        let val = query[1];

        if qt == 1 {
            ans += val * nx;
            ny -= val;
        }
        else {
            ans += val * ny;
            nx -= val;
        }

        println!("{ans}");
    });
}
