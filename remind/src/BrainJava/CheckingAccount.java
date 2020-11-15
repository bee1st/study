package BrainJava;

class CheckingAccount extends Account {
	String cardNo;
	CheckingAccount (String accountNo, String ownerName, int balance, String cardNo) {
		super(accountNo, ownerName, balance); //super클래스의 생성자 호출
		this.cardNo = cardNo;
		
	}

	int pay(String cardNo, int amount) throws Exception{
		if(!cardNo.equals(this.cardNo) || (balance < amount))
			throw new Exception("지불 불가");
		return withdraw(amount);
	}
}
