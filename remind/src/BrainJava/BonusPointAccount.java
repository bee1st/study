package BrainJava;

public class BonusPointAccount extends Account {
	int bonusPoint;
	BonusPointAccount (String accountNo, String ownerName, int balance, int bonusPoint) {
		super(accountNo, ownerName, balance);
		this.bonusPoint = bonusPoint;
		
	}
	void depoist(int amount) { //예금기능을 다시 구현하는 메소드
		//balance += amount;
		super.deposit(amount);
		bonusPoint += (int) (amount * 0.001);
	}
}

