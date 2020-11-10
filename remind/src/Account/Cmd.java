package Account;

import java.io.File;
import java.io.InputStream;

//C:\Windows\System32


public class Cmd {

	public static void main(String[] args) throws Exception{
		File f = new File("C:\\Windows\\System32", "cmd.exe");
		InputStream is = System.in; 
		byte[] datas = new byte[100];
		System.out.print("입력 : ");
		
		int nameBytes = is.read(datas);  
		String cmd1 = new String(datas, 0, nameBytes-2);
		
		System.out.println("==> " + cmd1);
	
	}

}
