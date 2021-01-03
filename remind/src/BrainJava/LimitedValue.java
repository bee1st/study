package BrainJava;

public class LimitedValue {
	final static int Upper_Limit = 100; //상수 필드 선언
	int value;
	void setValue(int value) {
		if(value < Upper_Limit)
			this.value = value;
		else
			this.value = Upper_Limit; //상수 필드 사용
	}

}
