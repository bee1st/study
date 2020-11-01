package Polymophism;

public class CarEx {
	
	public static void main(String[] args) {
		Car car = new Car();
		
		for(int i = 1; i <= 5; i++) {
			int problem = car.run();
			switch(problem) {
			
			case 1 : System.out.println("앞왼 타이어 교체");
			car.tires[0] = new Hankook("앞왼", 15);
			break;
			case 2 : System.out.println("앞오른 타이어 교체");
			car.tires[1] = new Kumho("앞오른", 17);
			break;
			case 3 : System.out.println("뒤왼 타이어 교체");
			car.tires[2] = new Hankook("뒤왼", 14);
			break;
			case 4 : System.out.println("뒤오른 타이어 교체");
			car.tires[3] = new Kumho("뒤오른", 13);
			break;
			}
			
		}
		
	}

}
