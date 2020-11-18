package BrainJava;

import java.io.FileWriter;
import java.io.IOException;

public class ch10_test1 {

	public static void main(String[] args) {
		FileWriter writer = null;
		try {
			writer = new FileWriter("output.txt");
			String str1 = "내 귀는 소라껍질";
			String str2 = "바다 소리를 그리워 한다";
//	문제	for (int i = 0; i < str1.length(); i++)
//				writer.write(str1.charAt(i));
//			writer.write('\n');
//			for (int i = 0; i < str2.length(); i++)
//				writer.write(str2.charAt(i));
//			writer.write('\n');
			System.out.println(str1); //답
			System.out.println(str2);
		}
		catch(IOException e) {
			System.out.println("파일을 출력할 수 없습니다");
		}
		finally {
			try {
				writer.close();

			}
			catch(Exception e) {

			}
		}

	}

}
