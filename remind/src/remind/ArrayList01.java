package remind;

import java.util.ArrayList;

public class ArrayList01 {

	public static void main(String[] args) {
		ArrayList arr = new ArrayList();
		arr.add("문자열");
		arr.add(Math.PI);
		arr.add(7);
		arr.add(null);
		arr.add("7" + 5);
		
		for(Object obj : arr) {
			System.out.println(obj);
		}

	}

}
