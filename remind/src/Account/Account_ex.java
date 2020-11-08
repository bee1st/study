package Account;

public class Account_ex {

	public static void main(String[] args) {
		Account obj1 = new Account("1111-3333-22222", "일이삼", 123123123);
		Account obj2 = new Account("888-4444-7777", "팔사칠", 847847847);
		
		obj1.input(555555);
		obj2.output(1111111);
		
		printAccount(obj1);
		printAccount(obj2);

	}
	static void printAccount(Account acc) {
		System.out.println("계좌번호 : " + acc.accountNo);
		System.out.println("예금주 : " + acc.ownerName);
		System.out.println("잔액 : " + acc.jango);
		System.out.println();
	}

}
