package remind;

import java.util.ArrayList;

public class ArrayList02 {

	public static void main(String[] args) {
		ArrayList number = new ArrayList();
		
		for(int i = 0; i < 10; i++) {
			number.add(i); //배열 크기 지정연습
		}
		
		int a = number.size();
		System.out.println(number);
		
		int b = (int)(Math.random() * 10);
		Object obj = number.get(b);
		System.out.println("b = " + b + " obj = " + obj); //의문? b와 obj의 값이 같다?
		
		for(Object c : number) {
			System.out.println(c);
		}
		
	}

}
