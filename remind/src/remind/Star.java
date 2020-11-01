package remind;

public class Star {
	public static void main(String[] args) {
		printStar("*", 30);
		System.out.println();
		System.out.println("Hello Java");
		printLine("-", 30);
	}
	
	static void printStar(String st, int num) {
		for(int i = 0; i < num; i++)
			System.out.print(st);
	}
	static void printLine(String st, int num) {
		for(int i = 0; i < num; i++)
			System.out.print(st);
	}

}
