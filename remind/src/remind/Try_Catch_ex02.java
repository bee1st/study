package remind;

public class Try_Catch_ex02 {
	public static void main(String[] args) {
		int[] divisor = {5, 4, 3, 2, 1, 0};
		for(int i = 0; i < 10; i++) {
			try {
				int share = 100 / divisor[i];
				System.out.println(share);
			}
			catch(java.lang.ArithmeticException e) {
				System.out.println("잘못된 연산입니다.");
			}
			catch(java.lang.ArrayIndexOutOfBoundsException e) {
				System.out.println("잘못된 인덱스입니다.");
			}
		}
		System.out.println("끝");
	}
}
