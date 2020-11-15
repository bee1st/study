package BrainJava;

public class RefTypeExample9 {

	public static void main(String[] args) {
		Account obj1 = new Account("111-22-333333333", "장화", 10000);
		CheckingAccount obj2 = (CheckingAccount) obj1; //타입 보증이 거짓으로 드러났다
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
