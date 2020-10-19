package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DeleteTest01 {

	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String user = "scott";
		String password ="tiger";
		Connection conn = null;
		PreparedStatement pstmt= null;


		try {
			//1.드라이버로딩
			Class.forName(driver);
			//2.Connection 객체얻기
			conn = DriverManager.getConnection(url, user, password);
			//3-1.쿼리문실행
			String sql = "delete from emp " + " where empno = 8000";
			pstmt = conn.prepareStatement(sql);
			//3-2.
			int cnt = pstmt.executeUpdate();
			//4.추가작업
			if (cnt > 0) {
				System.out.println("삭제되었습니다.");
			}else {
				System.out.println("삭제에 실패했습니다.");
			}
		}
		catch(Exception e) {

		}
		finally {
			try {
				if (pstmt != null) {
					pstmt.close();
				}
				if (conn != null) {
					conn.close();
				}

			}catch(Exception e) {
				e.printStackTrace();
			}
		}



	}


}


