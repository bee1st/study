package remind;

public class SubscriberInfo {
	String name, id, password;
	String PhoneNo, address;
	
	SubscriberInfo() {}
	
	SubscriberInfo(String name, String id, String password){
		this.name = name;
		this.id = id;
		this.password = password;
		
	}
	SubscriberInfo(String name, String id, String password, String PhoneNo, String address){
		this.name = name;
		this.id = id;
		this.password = password;
		this.PhoneNo = PhoneNo;
		this.address = address;
		
	}
	
	void changePassword(String password) {
		this.password = password;
	}
	
	void setPhoneNo(String PhoneNo) {
		this.PhoneNo = PhoneNo;
	}
	void setaddres(String address) {
		this.address = address;
	}
	

}
