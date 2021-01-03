package BrainJava;

import java.io.DataInputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class DataInputExample1 {

	public static void main(String[] args) {
		DataInputStream in = null;
		try {
			in = new DataInputStream(new FileInputStream("output.dat"));
			while(true) {
				int data = in.readInt();
				System.out.println(data);
			}
		} catch (FileNotFoundException fnfe) {
			System.out.println("파일이 존재하지 않습니다");
		} catch (EOFException eofe) {
			System.out.println("끝");
		} catch(IOException e) {
			System.out.println("파일을 읽을 수 없습니다");
		}finally {
			try {
				in.close();
			}
			catch(Exception e) {

			}
		}
	}

}
