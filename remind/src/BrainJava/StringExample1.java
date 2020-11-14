package BrainJava;

public class StringExample1 {

	public static void main(String[] args) {
		String str = "자바 커피";
		int len = str.length();
		for(int i = 0; i < len; i++) {
			char ch = str.charAt(i);
			System.out.println(ch);
		}

	}

}
