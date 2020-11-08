package BrainJava;

public class ch5_test2 {
	final int sideLength; //final 생성자이기때문에 
	void setSideLength(int sideLength) { //setSideLength가 아니라 클래스명인 ch5_test2 가 되야한다
										//set은 값을 저장하게 하는 메소드기때문에 final 에서 사용하면 안됨
	//void ch5_test2(int sideLength) 로 바꿔야한다
		this.sideLength = sideLength;
	}

}


