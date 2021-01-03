package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

//JDBC : DB연동여부 테스트
public class JdbcTest {
	//field
	//constructor
	//JdbcTest(){ System.out.println("JdbcTest()기본생성자야"); }

	//method
	public static void main(String[] args) {
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String user= "scott";
		String password="tiger";

		Connection conn = null;
		Statement stmt = null;

		//JdbcTest  jt = new JdbcTest();
		//참조변수.필드
		//참조변수.함수();

		//1.JDBC 드라이버 로드
		/*JDBC 드라이버를 로드하기 위해 드라이버 클래스 파일을 로드한다. 
		   자바의 Class 클래스의 forName() 메소드를 이용하면 특정 클래스 파일을 읽어 들일 수 있다.*/
		//mySql이면  Class.forName("com.mysql.jdbc.Driver");
		//Oracle   
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("정상적으로 JDBC 드라이버 로드하였어요");	

			//2.자바 응용프로그램과 JDBC의 연결
			/*DriverManager는 자바 응용프로그램을 JDBC 드라이버에 연결시켜주는 클래스이다.
		  DriverManager.getConnection() 메소드를 호출하여 
		   데이터베이스에 연결하고 Connection 객체를 반환한다.
		  Connection java.sql.DriverManager.getConnection(String url, String user, String password)*/

			conn = DriverManager.getConnection(url, user, password);
			System.out.println("Connection얻기 성공");

			//3.쿼리실행할 객체를 생성 및 쿼리실행
			/*자바에서 SQL문을 실행하기 위해서는 Statement 클래스 */
			//쿼리실행할 객체를 생성
			stmt = conn.createStatement();
			System.out.println("Statement객체 생성 성공");
			//쿼리실행
			//쿼리문 주의사항, 문법,데이터타입,;포함x, 공백
			/*int executeUpdate(String sql): INSERT,UPDATE,DELETE sql문을 실행하고, 
			   								sql문 실행으로 영향을 받은 행의 개수나 0을 반환*/
			//int cnt = stmt.executeUpdate("DELETE FROM DEPT WHERE deptno=90");
			//int cnt = stmt.executeUpdate("INSERT INTO DEPT VALUES(90,'IT','서울')");
			int cnt = stmt.executeUpdate("UPDATE DEPT SET loc='독도' WHERE deptno=90");
			if(cnt>0) { 
				System.out.println("쿼리가 정상적으로 실행 cnt="+cnt); 
			}else {
				System.out.println("쿼리가 정상적으로 x cnt="+cnt); 
			}

		} catch (ClassNotFoundException e) {//Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("JDBC 드라이버 로드실패");
			e.printStackTrace();
		} catch (SQLException e) {
			System.out.println("SQL관련 에러발생");
			e.printStackTrace();
		}finally {
			//자원반납을 반드시 하게하려면 finally블럭안에 코드작성
			//finally 블럭에는
			//catch절에 들어가던 들어가지않던
			//무조건 실행해야하는 코드를 작성한다
			//예) DB연동시의 자원반납 
			System.out.println("finally블럭안");

			if( stmt!=null ) {					
				try {
					stmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}

			if( conn!=null ) {					
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}

		}



	}//main

}//class





