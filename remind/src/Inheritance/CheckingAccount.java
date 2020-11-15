package Inheritance;

class CheckingAccount extends Account {
	String cardNo;
	int pay(String cardNo, int amount) throws Exception {
		if (!cardNo.equals(this.cardNo) || (balance < amount))
			throw new Exception("지불불가");
		return withdraw(amount);
	}

}
