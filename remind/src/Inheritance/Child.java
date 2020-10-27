package Inheritance;

public class Child extends Parent {
	
	public void c1() {System.out.println("자식호출1");}
	
	@Override
	public void p2() {System.out.println("오버라이드");}
	
	public void c3() {System.out.println("자식호출3");}

}
