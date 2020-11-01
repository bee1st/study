package remind;

public class Number_ex {

	public static void main(String[] args) {
		int[] num = new int[10];
		for(int i = 0; i < num.length; i++) {
			num[i]= i + 1;
			int arr =num[i];
		}
		
		
		Number obj = new Number(num);
		int total = obj.getTotal();
		int avg = obj.getAverage();
		System.out.println("합계 = " + total);
		System.out.println("평균 = " + avg);
		

	}

}
