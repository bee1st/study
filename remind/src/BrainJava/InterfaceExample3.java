package BrainJava;

public class InterfaceExample3 {

	public static void main(String[] args) {
		SeparateVolume obj = new SeparateVolume("864q", "나무", "베르나르베르베르");
		printState(obj);
		obj.checkOut("이수경", "20200123");
		printState(obj);

	}
	static void printState(SeparateVolume obj) {
		if(obj.state == Lendable.STATE_NORMAL) {
			System.out.println("----------------------");
			System.out.println("대출상태 : 대출가능");
			System.out.println("----------------------");
		}
		if(obj.state == Lendable.STATE_BORROWED) {
			System.out.println("----------------------");
			System.out.println("대출상태 : 대출중");
			System.out.println("대출인 : " + obj.borrower);
			System.out.println("대출일 : " + obj.checkOutDate);
			System.out.println("----------------------");
		}
	}

}
