package BrainJava;

public class InterfaceExample2 {

	public static void main(String[] args) {
		Lendable arr[] = new Lendable[3];
		arr[0] = new SeparateVolume("883d326b2", "푸코의 진자", "에코");
		arr[1] = new SeparateVolume("563d356b2", "서양미술사", "곰브리치");
		arr[2] = new AppCDInfo("2020-0621", "자바프로그래밍");
		checkOutAll(arr, "윤지혜", "20200315");
	}
	static void checkOutAll(Lendable arr[], String borrower, String date) {
		for(int i = 0; i < arr.length; i++)
			try {
				arr[i].checkOut(borrower, date);
			} catch (Exception e) {
				e.printStackTrace();
			}
		
	}

}