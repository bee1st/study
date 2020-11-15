package BrainJava;

public class InterfaceExample1 {

	public static void main(String[] args) {
		SeparateVolume obj1 = new SeparateVolume("863?774개", "개미", "베르나르베르베르");
		
		AppCDInfo obj2 = new AppCDInfo("2020-0115", "John kim");
		obj1.checkOut("영희", "20201112");
		obj2.checkOut("철수", "20200812");
		obj1.checkIn();
		obj2.checkIn();
		
		

	}

}
