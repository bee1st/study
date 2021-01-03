package BrainJava;

public class ch5_test4 {
	static int lastseqNo = 0; //정적 필드 선언
	int seqNo;
	String writer;
	String writtenDate;
	String title;
	String content;
	
	ch5_test4(String writer, String writtenDate, String title, String content) {
		this.seqNo = ++lastseqNo;
		this.writer = writer;
		this.writtenDate = writtenDate;
		this.title = title;
		this.content = content;
		
	}

}
