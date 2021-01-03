package remind;

public class For {
	public static void main(String[] args) {
		for(int i = 1; i <= 100; i++ ) {
			System.out.println();
			System.out.printf("i = %d ", i);
			
			
			int a = i;
			
			do {
				if(a % 10 % 3 == 0 && a % 10 != 0)
					System.out.print("짝");
			}
			while((a /= 10) != 0);
		}
		System.out.println();
	}
}
