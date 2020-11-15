package BrainJava;

public interface ch6_MessageSender {
	//title, senderName 필드는 final static 키워드가 없지만 인터페이스 안에있기때문에 자동으로 붙는
	String title; //첫번째 인터페이스의 상수필드는 선언할때 반드시 초기값 대입
	String senderName; //두번째 인터페이스는 생성자를 가질수 없기때문
	ch6_MessageSender(String title, String senderName) {
		this.title = title;
		this.senderName = senderName;
	}
	abstract void sendMessage(String recipient);
}
