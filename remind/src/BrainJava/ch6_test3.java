package BrainJava;

public class ch6_test3 {

	public static void main(String[] args) {
		Lendable arr[] = {
				new AppCDInfo("2005-7001", "Redhat Fedora"),
				new SeparateVolume("859q986c", "책상은 책상이다", "빅셀") 
		};
		checkOutAll(arr, "김수진", "20060318");
	}
	static void checkOutAll(Lendable arr[], String borrower, String date) {
		for(Lendable obj : arr) {
			try {
				obj.checkOut(borrower, date);
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println("대출인 : " + borrower);
			System.out.println("대출일 : " + date);

		}
	}

}
