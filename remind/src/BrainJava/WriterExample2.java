package BrainJava;

import java.io.*;

public class WriterExample2 {

	public static void main(String[] args) {
		BufferedWriter writer = null;
		try {
			writer = new BufferedWriter(new FileWriter("output.txt"));
			char arr[] = {'뇌', '를', ' ', '자', '극', '하', '는', ' ', 'p', 'y', 't', 'h', 'o', 'n'};
			for(int i = 0; i < arr.length; i++) {
				writer.write(arr[i]);
			}
		} catch (IOException e) { 
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
