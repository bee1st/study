package BrainJava;

public class RefTypeExample7 {
	
	public static void main(String[] args) {
		Account obj = new CheckingAccount("111-22-33333333", "홍련", 100000, "4444-5555-6666-8888");
		CheckingAccount obj2 = obj1; //잘못된 대입문

		try {
			int amount = obj2.pay("5555-6666-7777-8888", 47000);
			System.out.println("인출액 : " + amount);
			System.out.println("카드번호 : " + obj2.cardNo);
		}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
