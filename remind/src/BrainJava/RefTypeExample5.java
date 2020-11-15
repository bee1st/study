package BrainJava;

public class RefTypeExample5 {

	public static void main(String[] args) {
		Point obj = null;
		if(obj == null) {
			System.out.println("obj변수가 가리키는 객체가 없습니다");
			return;
		}
		System.out.println(obj.x);
		System.out.println(obj.y);

	}

}
