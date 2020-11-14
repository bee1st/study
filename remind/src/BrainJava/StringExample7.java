package BrainJava;

public class StringExample7 {

	public static void main(String[] args) {
		String str1 = "   Let it be.   ";
		String str2 = str1.trim();
		System.out.println(str2); //Let it be.
		System.out.println(str2.concat("Speaking words of wisdom.")); //Let it be.Speaking words of wisdom.
		System.out.println(str2.toUpperCase());//LET IT BE.
		System.out.println(str2.toLowerCase());//let it be.
		System.out.println(str2.replace("e", "a")); //Lat it ba;
		System.out.println(str1); //   Let it be.   
		System.out.println(str2); //Let it be.

	}

}
