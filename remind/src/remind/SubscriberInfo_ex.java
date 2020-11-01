package remind;

public class SubscriberInfo_ex {

	public static void main(String[] args) {
		SubscriberInfo obj1 = new SubscriberInfo("흥부", "poorman", "givemoney");
		SubscriberInfo obj2 = new SubscriberInfo("놀부", "richrich", "alotofmoney", "112-119", "펜트하우스");
		
		sinsang(obj1);
		sinsang(obj2);
		
		}
		static void sinsang(SubscriberInfo obj) {
			System.out.println("이름 : " + obj.name);
			System.out.println("아이디 : " + obj.id);
			System.out.println("비밀번호 : " + obj.password);
			System.out.println("전화번호 : " + obj.PhoneNo);
			System.out.println("주소 : " + obj.address);
			System.out.println();
			
		}
			
		

	

}
