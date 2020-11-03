package remind;

public class Numbers_Method_ex02 {

	public static void main(String[] args) {
		int[] arr = new int[0];
		Numbers obj = new Numbers(arr);
		try {
			int average = obj.getAverage();
			System.out.println("평균 = " + average);
		}
		catch(Exception e) {
			System.out.println("평균을 계산하는 도중 에러 발생");
		}

	}

}
