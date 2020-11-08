package BrainJava;

public class Account {
	String accountNo;
	String ownerName;
	int balance;

	//선언문
	public Account (String accountNo, String ownerName, int balance) {
		this.accountNo = accountNo;
		this.ownerName = ownerName;
		this.balance = balance; 			

	}

	//예금한다
	void deposit(int amount) {
		balance += amount; 
	}

	//인출한다
	public int withdraw(int amount) throws Exception { 
		if (balance < amount)
			//return 0;
			throw new Exception("잔액부족");
		balance -= amount;
		return amount;
	}
}


