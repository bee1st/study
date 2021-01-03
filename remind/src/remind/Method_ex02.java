package remind;

public class Method_ex02 {
	public static void main(String[] args) {
		printStar("*", 17);
		System.out.println();
		System.out.println("*"+ " 메소드 공부중 " + "*");
		printStar("*", 17);
		
	}
	
	static void printStar(String a, int b) {
		for(int i = 0; i < b; i++) {
			System.out.print(a);

		}
	}
}
