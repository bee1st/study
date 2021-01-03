package BrainJava;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class FileExample2 {

	public static void main(String[] args) {
		FileWriter writer = null;
		try {
			File file = File.createTempFile("tmp", ".txt", new File("C:\\Temp")); //임시 파일 생성
			writer = new FileWriter(file);
			writer.write('자');
			writer.write('바');
		}
		catch (IOException e) {
			System.out.println("임시 파일에 쓸 수 없습니다.");
		} 
		finally{
			try {
				writer.close();
			}
			catch(Exception e) {
			}
		}
	}
}
