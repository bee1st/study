package remind;

import java.util.Scanner;

public class For2 {

	public static void main(String[] args) {
		int user;
		int num = (int)(Math.random() * 7);
		Scanner dice = new Scanner(System.in);
		user = dice.nextInt();

		if(user == num) {
			System.out.println("맞췄습니다");
		}else {
			System.out.println("다시");
		}
	}
}


