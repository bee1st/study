package remind;

import static org.junit.Assert.*;

import org.junit.Test;

public class Cal_ex {

	@Test
	public void testcal() {
		CalTest t1 = new CalTest();
		
		int result1 = t1.add(100, 200);
		assertEquals(300,result1);
		System.out.println("결과 : " + result1);
		String result2 = t1.str1("K", "K");
		assertEquals("K",result2);
		System.out.println("결과 : " + result2);
		int result3 = t1.minus(100, 400);
		assertEquals(-300, result3);
		System.out.println("결과 : " + result3);
		long result4 = t1.divide(100, 0);
		assertEquals(0, result4);
		System.out.println("결과 : " + result4);
		int result5 = t1.add(-1000, 200);
		assertEquals(-800,result5);
		System.out.println("결과 : " + result5);
		String result6 = t1.str2("훈민정음", "한글");
		assertSame("한글",result6);
		System.out.println("결과 : " + result6);
		
		
	}


}
