use std::f64::consts::PI;
use proconio::input;

fn main() {
    input!{
        D: f64,
    }

    let x = D / 2.0;
    
    println!("{}", x * x * PI);
}
