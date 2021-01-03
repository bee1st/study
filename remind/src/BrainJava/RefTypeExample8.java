package BrainJava;

public class RefTypeExample8 {

	public static void main(String[] args) {
		Account obj1 = new CheckingAccount("111-22-3333333", "홍길동", 10000, "4444-5555-7777-8888");
		CheckingAccount obj2 = (CheckingAccount) obj1; //캐스트연산자 (CheckingAccount)
		try {
			int amount = obj2.pay("4444-5555-7777-8888", 4700);
			System.out.println("인출액 : " + amount);
			System.out.println("카드번호 : " + obj2.cardNo);
		}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}

	}

}
