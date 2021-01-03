package BrainJava;

public class Physical_ex01 {

	public static void main(String[] args) {
		PhysicalInfo phy = new PhysicalInfo("혜리", 10, 158.9f, 43.3f);
		printPhysicalInfo(phy);
		phy.update(11, 163.2f, 53.3f);
		printPhysicalInfo(phy);
		phy.update(12, 164.3f);
		printPhysicalInfo(phy);
		phy.update(13);
		printPhysicalInfo(phy);

	}
	
	static void printPhysicalInfo(PhysicalInfo phy) {
		System.out.println("이름 : " + phy.name);
		System.out.println("나이 : " + phy.age);
		System.out.println("키 : " + phy.height);
		System.out.println("몸무게 : " + phy.weight);
		System.out.println();
	}

}
