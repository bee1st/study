package Inheritance;

public class InheritanceExample1 {

	public static void main(String[] args) {
		CheckingAccount obj = new CheckingAccount();
		obj.accountNo = "111-22-33333333";
		obj.ownerName = "홍련";
		obj.cardNo = "5555-4444-7777-8888";
		obj.deposit(1000000);
		
		int paidAmount;
		try {
			paidAmount = obj.pay("5555-4444-7777-8888", 470000);
			System.out.println("지불액 : " + paidAmount);
			System.out.println("잔액 : " + obj.balance);
		} catch (Exception e) {
			String msg = e.getMessage();
			System.out.println(msg);
		}
	}

}
