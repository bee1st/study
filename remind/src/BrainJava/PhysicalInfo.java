package BrainJava;

public class PhysicalInfo {
	String name;
	int age;
	float height, weight;
	
	//생성자
	PhysicalInfo(String name, int age, float height, float weight) {
		this.name = name;
		this.age = age;
		this.height = height;
		this.weight = weight;
	}
	
	//오버로드 된 메소드1
	void update(int age) {
		this.age = age;
	}
	
	//오버로드 된 메소드2
	void update(int age, float height) {
		this.age = age;
		this.height = height;
		
	}
	
	//오버로드 된 메소드3
	void update(int age, float height, float weight) {
		this.age = age;
		this.height = height;
		this.weight = weight;
	}

}
