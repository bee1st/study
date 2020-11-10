package Account;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

//C:\Windows\System32
public class Cmd {

	public static void main(String[] args) {
		Runtime rt = Runtime.getRuntime();
		String exeFile = "C:\\Windows\\System32\\cmd.exe";
		System.out.println("exeFile: " + exeFile);
		Process p;

		try {
			p = rt.exec(exeFile);
			p.waitFor();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}