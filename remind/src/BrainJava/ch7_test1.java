package BrainJava;

public class ch7_test1 {

	public static void main(String[] args) {
		Account obj1 = new Account("111-22-333333", "홍길동", 10000);
		Account obj2 = new Account("777-88-999999", "임꺽정", 30000);
		Account obj3 = new CheckingAccount("444-55-666666", "장길산", 50000, "5555-6666-7777-8888");
		Account obj4 = new Account("000-00-000000", "김미영", 0);
		printAccountInfo(obj1);
		printAccountInfo(obj2);
		printAccountInfo(obj3);
		printAccountInfo(obj4);

	}
	static void printAccountInfo(Account obj) {
		System.out.println("계좌번호 : " + obj.accountNo);
		System.out.println("예금주 : " + obj.ownerName);
		System.out.println("잔액 : " + obj.balance);
		if(obj instanceof CheckingAccount) {
			CheckingAccount ca = (CheckingAccount) obj;
			System.out.println("카드번호 : " + ca.cardNo);
		}
		System.out.println();
	}
	

}
