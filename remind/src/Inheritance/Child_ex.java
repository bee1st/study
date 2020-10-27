package Inheritance;

public class Child_ex {

	public static void main(String[] args) {
		
		Child child = new Child();
		Parent parent = child;
		
		parent.p1();
		parent.p2();
		parent.p3();
		System.out.println();
		
		GrandChild grandchild = new GrandChild();
		parent = grandchild;
		
		parent.p1();
		parent.p2();
		parent.p3();
		System.out.println();
		
		parent.p1();
		parent.p2();
		parent.p3();
		System.out.println();
		

	}

}
