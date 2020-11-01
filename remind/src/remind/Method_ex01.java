package remind;

import java.util.Scanner;

public class Method_ex01 {

	public static void main(String[] args) {
		int num1;
		int num2;
		int result;
		Scanner sc = new Scanner(System.in);
		System.out.println("처음 숫자를 입력하세요 : ");
		num1 = sc.nextInt();
		System.out.println("두번째 숫자를 입력하세요 : ");
		num2 = sc.nextInt();
		result = add(num1, num2);
		System.out.println("두 숫자 더한 값 : " + result);

	}
	
	static int add(int a, int b) {
		int sum;
		sum = a + b;
		return sum;
	}

}
