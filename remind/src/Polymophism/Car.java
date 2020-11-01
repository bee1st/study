package Polymophism;

public class Car {
	String Brand;
	int Price;
	String wheel;

	Tire[] tires = {new Tire("앞왼", 4), new Tire("앞오른", 5), new Tire("뒤왼", 3), new Tire("뒤오른", 2)};
	
	public Car() {}

	int run() {
		System.out.println("전진");
		for(int i = 0; i < tires.length; i++) {
			if(tires[i].roll() == false) {
				stop();
				return (i + 1);
			}
		}
		return 0;
	}
	void stop() {
		System.out.println("멈춰");


	}
}

