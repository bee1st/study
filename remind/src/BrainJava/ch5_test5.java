package BrainJava;

public class ch5_test5 {
	public static void main(String[] args) {
		printCharacter('*', 30);
		System.out.println("hellow java");
		printCharacter('-', 30);
	}
	
	static void printCharacter (char ch, int num) {
		for (int i = 0; i < num; i++) {
			System.out.println(ch);
		}
		System.out.println();
	}

}
