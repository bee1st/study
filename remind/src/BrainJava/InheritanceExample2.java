package BrainJava;

public class InheritanceExample2 {

	public static void main(String[] args) {
		CheckingAccount obj = new CheckingAccount("111-22-33333333", "장화", 0, "5555-2222-7777-9999");
		obj.deposit(1000000);
		
		int paidAmount;
		try {
			paidAmount = obj.pay("5555-2222-7777-9999", 470000);
			System.out.println("지불액 : " + paidAmount);
			System.out.println("잔액 : " + obj.balance);
		} catch (Exception e) {
			String msg = e.getMessage();
			System.out.println(msg);
		}

	}

}
