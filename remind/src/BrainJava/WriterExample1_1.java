package BrainJava;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriterExample1_1 {

	public static void main(String[] args) {
		BufferedWriter writer = null;
		try {
			writer = new BufferedWriter(new FileWriter("output.txt"));
			char arr[] = {'뇌', '를', ' ', '자', '극', '하', '는', ' ', 'J', 'A', 'V', 'A'};
			for(int i = 0; i < arr.length; i++) {
				writer.write(arr[i]);
			}
		} catch (IOException e) { //FileWriter 생성자는 IOException 을 발생한다
			System.out.println("파일을 출력할 수 없습니다.");
		}
		finally {
			try {
				writer.close();
			} catch (Exception e) {
			}
		}

	}

}
