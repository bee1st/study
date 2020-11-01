package remind;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ArrayListVSLinkedList {

	public static void main(String[] args) {
		long StartTime;
		long EndTime;
		
		List<String> list1 = new ArrayList<String>();  //<> 지네릭
		List<String> list2 = new LinkedList<String>();
		
		StartTime = System.nanoTime();
		for(int i = 0; i < 10000; i++) {
			list1.add(0, String.valueOf(i)); //0부터 i번까지 배열에 넣어준다
		}
		
		EndTime = System.nanoTime();
		System.out.println("list1 = " + (EndTime - StartTime));
		System.out.println("VS");
		
		for(int i = 0; i < 10000; i++) {
			list2.add(0, String.valueOf(i));
		}
		EndTime = System.nanoTime();
		System.out.println("list2 = " + (EndTime - StartTime));
		
		
	}

}
