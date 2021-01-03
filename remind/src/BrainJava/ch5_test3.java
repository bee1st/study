package BrainJava;

public class ch5_test3 {
	int width, height;
	ch5_test3 (int width, int height) throws Exception { //필드에서 throws 하거나
		if (width  <= 0 || height <= 0) {
			throw new Exception("안돼!!");
		}
		this.width = width;
		this.height = height;
		
	}

	int getArea() throws Exception { //메소드에서 throws 하거나
		if (width  <= 0 || height <= 0) {
			throw new Exception("안돼!!");
		}
		return width * height;
	}
}
