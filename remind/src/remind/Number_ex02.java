package remind;

public class Number_ex02 {

	public static void main(String[] args) {
		int[] arr = new int[0];
		Number obj = new Number(arr);
		try {
			int average = obj.getAverage();
			System.out.println("평균 = " + average);
		}
		catch (Exception e) {
			System.out.println("에러발생");
		}

	}

}
