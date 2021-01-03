package BrainJava;

public class InheritanceExample6 {

	public static void main(String[] args) {
		EmailSender obj1 = new EmailSender("생일을 축하합니다", "고객센터", "admin@admin.net", "10% 할인쿠폰이 발송되었습니다.");
		SMSSender obj2 = new SMSSender("생일을 축하합니다", "고객센터", "admin@admin.net", "10% 할인쿠폰이 발송되었습니다.");
		
		obj1.sendMessage("dangchum@nice.com");
		obj1.sendMessage("congratulation@hahaha.com");
		obj2.sendMessage("114-1115");

	}

}
