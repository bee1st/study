package BrainJava;

public class Account_ex01 {

	public static void main(String[] args) throws Exception {
		Account obj1 = new Account ("111-222-33333333", "김영식", 2000000);
		Account obj2 = new Account ("333-444-77777777", "박진희", 70000000);
		obj1.deposit(1000000);
		obj2.withdraw(20000);
		printAccount(obj1);
		printAccount(obj2);

	}
	
	static void printAccount(Account obj) {
		System.out.println("계좌번호 : " + obj.accountNo);
		System.out.println("예금주 이름 : " + obj.ownerName);
		System.out.println("잔액 : " + obj.balance);
		System.out.println();
		
	}

}
