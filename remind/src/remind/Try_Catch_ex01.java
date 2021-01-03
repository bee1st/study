package remind;

public class Try_Catch_ex01 {
	public static void main(String[] args) {
		int a = 3, b = 0;
		int result;
		try {
			result = a / b;
			System.out.println(result);
		}
		catch(java.lang.ArithmeticException e){
			System.out.println("잘못된 연산입니다.");
		}
		finally {
			System.out.println("Done");
		}
	}
}
