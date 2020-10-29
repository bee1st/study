package remind;

public class Account {
	String accountNo;
	String ownerName;
	int jango;
	
	Account(String accountNo, String ownerName, int jango){
		this.accountNo = accountNo;
		this.ownerName = ownerName;
		this.jango = jango;
	}
	
	void input(int Mymoney) {
		jango += Mymoney;
	}
	int output(int Mymoney) {
		if(jango < Mymoney) {
			return 0;
		} else {
			jango -= Mymoney;
			return jango;
		}
	}

}
