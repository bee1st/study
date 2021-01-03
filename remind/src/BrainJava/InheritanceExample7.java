package BrainJava;

public class InheritanceExample7 {
	public static void main(String[] args) {
		Account obj1 = new Account("111-22-333333", "임꺽정", 10000);
		CheckingAccount obj2 = new CheckingAccount("333-88-555555", "홍길동", 40000, "5555-7777-6666-1111");
		CreditLineAccount obj3 = new CreditLineAccount("222-88-999999", "김삿갓", 20000, 5000000);
		BonusPointAccount obj4 = new BonusPointAccount("888-66-444444", "허생", 0, 0);
		
		System.out.println(obj1);
		System.out.println(obj2);
		System.out.println(obj3);
		System.out.println(obj4);
	}
	static void printAccountInfo(Account obj) {
		System.out.println("계좌번호 : " + obj.accountNo);
		System.out.println("예금주 이름 : " + obj.ownerName);
		System.out.println("잔액 : " + obj.balance);
		System.out.println();
	}

}
