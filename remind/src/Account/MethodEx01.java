package Account;

public class MethodEx01 {

	public static void main(String[] args) {
		Account obj1 = new Account("111-222-33333333", "심봉사", 2000000);
		Account obj2 = new Account("555-222-44444444", "용궁해마", 1000000);
		obj1.input(1000000);
		obj2.output(2000000);
		printAccount(obj1);
		printAccount(obj2);
	}
	static void printAccount(Account obj) {
		System.out.println("계좌번호 : " + obj.accountNo);
		System.out.println("예금주 이름 : " + obj.ownerName);
		System.out.println("잔액 : " + obj.jango);
		System.out.println();
	}

}
