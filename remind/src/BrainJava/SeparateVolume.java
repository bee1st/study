package BrainJava;

public class SeparateVolume implements Lendable{
	String requestNo;
	String bookTitle;
	String writer;
	String borrower;
	String checkOutDate;
	byte state;
	SeparateVolume(String requestNo, String bookTitle, String writer) {
		this.requestNo = requestNo;
		this.bookTitle = bookTitle;
		this.writer = writer;
		
	}													//컴파일 오류 메소드 구현 불가
	public void checkOut(String borrower, String date) /*throws Exception*/ {
		
		if (state != STATE_NORMAL) //Lendable 인터페이스의 상수필드 사용
//		if (state != 0) 
//			throw new Exception("대출불가 : " + bookTitle);
		return;
		this.borrower = borrower;
		this.checkOutDate = date;
		this.state = STATE_BORROWED; //Lendable 인터페이스의 상수필드 사용
		System.out.println("*" + bookTitle + "이(가) 대출되었습니다.");
		System.out.println("대출인 : " + borrower);
		System.out.println("대출일 : " + date + "\n");		
	}
	public void checkIn() {
		this.borrower = null;
		this.checkOutDate = null;
		this.state = STATE_NORMAL; //Lendable 인터페이스의 상수필드 사용
		System.out.println("*" + bookTitle + "이(가) 반납되었습니다.");
	}
}
