package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

//DB연동 - select 쿼리문 실행

public class SelectTest {
	public static void main(String[] args) {

		//1. JDBC 드라이버 로드
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("정상적으로 JDBC 드라이버 로드하였어요");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		//2. 자바 응용프로그램과 JDBC의 연결
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String user= "scott";
		String password="tiger";
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null; // 쿼리실행결과를 저장할 변수 선언
		String sql = null; //실행할 쿼리문을 저장할 변수 선언
		try {
			conn = DriverManager.getConnection(url, user, password);

			//3-1. 쿼리실행할 객체들 생성
			stmt = conn.createStatement();

			//3-2. 쿼리실행

			sql = "select deptno, dname, loc";
			sql += " from DEPT ";
//			sql += "where deptno = 90";

			rs = stmt.executeQuery(sql);
			
			//콘솔출력
			while(rs.next()) {
				//rs.getXxx(String타입의 컬럼명)
//				int deptno = rs.getInt("deptno");
//				String dname = rs.getString("dname");
//				String loc = rs.getString("loc");
//				System.out.println(deptno + "\t" + dname + "\t" + loc);
				//rs.getXxx(int columnIndex) : select문의 컬럼순서를 제시
				int deptno = rs.getInt(1); //여기에서는 select 문의 첫번째 컬럼인 deptno
				String dname = rs.getString(2);
				String loc = rs.getString(3);
				System.out.println(deptno + "\t" + dname + "\t" + loc);
			
			
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {

			//4. 자원반납 -나중에 사용한 객체부터 close()
			if(rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}

			}//finally

			if(stmt != null) { 
				try {
					stmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}//if
			if(conn != null) {
				try {
					conn.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
			}

		}//main
	}
}