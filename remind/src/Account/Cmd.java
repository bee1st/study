package Account;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;

public class Cmd {

	public static void main(String[] args) throws IOException {

		boolean stop = false;
		while(!stop) {

			InputStream is = System.in; 
			byte[] datas = new byte[100];
			System.out.println("시스템 종료하려면 exit를 입력하세요");
			System.out.print("검색(ex c:\\, D:\\study, ..) : ");
			
			int nameBytes = is.read(datas);
			String name = new String(datas, 0, nameBytes-2);

			File dir = new File(name);

			if(dir.exists()) {
				String[] list = dir.list();

				for(String fileName : list) {
					System.out.println(fileName);
				}
			} else if(name.equals("exit")) {
				break;
				
			}else if(!dir.exists()){
				System.out.println("파일이 없습니다");
				
			}
		}
		
		System.out.println("시스템이 종료되었습니다.");
	}	

}
