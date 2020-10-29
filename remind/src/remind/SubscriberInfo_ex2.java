package remind;

public class SubscriberInfo_ex2 {
	public static void main(String[] args) {
		SubscriberInfo obj = new SubscriberInfo();
		example(obj);
	}
	
	

	static void example(SubscriberInfo obj) {
		System.out.println("이름 : " + obj.name);
		System.out.println("아이디 : " + obj.id);
		System.out.println("비밀번호 : " + obj.password);
		System.out.println("전화번호 : " + obj.PhoneNo);
		System.out.println("주소 : " + obj.address);
		System.out.println();
	}
}
