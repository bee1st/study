package BrainJava;

public class CreditLineAccount extends Account {
	int creditLine;
	CreditLineAccount (String accountNo, String ownerName, int balance, int creditLine) {
		super(accountNo, ownerName, balance);
		this.creditLine = creditLine;
	}
	public int withdraw (int amount) throws Exception{ //인출 기능을 다시 구현한 메소드
		if((balance + creditLine) < amount)
			throw new Exception("인출 불가");
		balance -= amount;
		return amount;
	}
	

}
