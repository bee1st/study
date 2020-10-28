package remind;

public class Boolean_ex01 {
	public static void main(String[] args) {
		int a, b;
		boolean c;
		
		a = (int)(Math.random()*10);
		b = (int)(Math.random()*10);
		
		if(a >= b) {
			System.out.println("a = " + a + " b = " + b + "이므로");
			c = true;
		}else {
			System.out.println("a = " + a + " b = " + b + "이므로");
			c = false;
		}
		System.out.println(c);
	}

}
