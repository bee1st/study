package jUniTest.ValidPW;

import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.Collection;

import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;


//단위테스트시 여러가지 입력밧에 대한 테스트를 한번에 수행할때
@RunWith(Parameterized.class)
public class ValidPWTest {
	private String password;
	private boolean isValid;
	private static ValidPW validator;


	//@BeforeClass는 test메서드를 run하기 전에 한번 실행. 정적변수의 값을 초기화할때 주로 사용
	@BeforeClass
	public static void setUp() {
		validator = new ValidPW();
	}

	public ValidPWTest(String password, boolean isValid) {
		this.password = password;
		this.isValid = isValid;
	}

	@Parameters
	public static Collection passwords() {
		return Arrays.asList(
				new Object[][] {
					{"123f",false},
					{"123",false},
					{"qwerasdf12",true},
					{"12345678",false},
					{"1q2w3e4r",true},
					{"qwerasdf",false}
				}
				);
	}
	@Test
	public void isValidPWWithParams() {
		assertEquals(validator.isValid(this.password), this.isValid);


	}


}
