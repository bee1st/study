package BrainJava;

public class StringChanger {

	public static void main(String[] args) {
		String str1 = "뇌를 자극하는 C";
		String str2 = str1.replace("C", "하드웨어");
		String str3 = str2.concat("입문");
		System.out.println(str1);
		System.out.println(str2);
		System.out.println(str3);

	}

}
