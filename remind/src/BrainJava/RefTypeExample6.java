package BrainJava;

public class RefTypeExample6 {
	public static void main(String[] args) {
		Account obj = new CheckingAccount("111-22-33333333", "홍련", 10, "4444-5555-6666-7777");
		
		try {
			int amount = obj.pay("4444-5555-6666-7777", 47000);
			System.out.println("인출액 : " + amount);
			System.out.println("카드번호 : " + obj.cardNo);
		}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
