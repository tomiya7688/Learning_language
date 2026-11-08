// 信号が取り得る3つの状態
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

// 信号の状態に合わせて案内を返す
fn instruction(light: &TrafficLight) -> &'static str {
    match light {
        TrafficLight::Red => "止まる",
        TrafficLight::Yellow => "注意する",
        TrafficLight::Green => "進む",
    }
}

fn main() {
    // すべての状態を順番に確かめる
    for light in [
        TrafficLight::Red,
        TrafficLight::Yellow,
        TrafficLight::Green,
    ] {
        println!("{}", instruction(&light));
    }
}
