package BrainJava;

import java.io.*;

public class ReaderExample1 {

	public static void main(String[] args) {
		try {
			FileReader reader;
			reader = new FileReader("poem.txt");
			while(true) {
				int data =reader.read();
				if(data == -1)
					break;
				char ch = (char) data;
				System.out.println(ch);
			}
			reader.close(); 
		}
		catch (FileNotFoundException fnfe) {
			System.out.println("파일이 존재하지 않습니다");

		} 
		catch (IOException ioe) { //이 익셉션이 발생하면  close 메소드가 실행되지 않은채 프로그램이 끝난다.
								 // 그래서 자원 할당받은걸 반환하지 않아 문제가 될 수 있다.
			System.out.println("파일을 읽을 수 없습니다.");
		}
	}
}
