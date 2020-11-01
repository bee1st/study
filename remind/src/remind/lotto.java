package remind;

public class lotto {

	public static void main(String[] args) {
		int[] lotto = new int[45];

		for(int i = 0; i < lotto.length; i++) 
			lotto[i] = i + 1;

		int a = 0;
		int b = 0;

		for(int i = 0; i < 6; i++) {
			b = (int)(Math.random() * 45);
			a = lotto[i];
			lotto[i] = lotto[b];
			lotto[b] = a;
		}

		for(int i = 0; i < 6; i++) 
			System.out.print(lotto[i] + "\n");

	}
}