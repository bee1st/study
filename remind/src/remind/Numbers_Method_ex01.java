package remind;

public class Numbers_Method_ex01 {
	public static void main(String[] args) {
		int arr[] = {10, 20, 30, 40, 50, 60, 70, 80};
		Numbers obj = new Numbers(arr);
		int total = obj.getTotal();
		int average = obj.getAverage();
		System.out.println("total = " + total);
		System.out.println("avg = " + average);
	}

}
