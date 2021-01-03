package jdbc;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SelectTest01 {

	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";		
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String user = "scott";
		String password ="tiger";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;

		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url,user,password);
			String sql = "select empno, ename, sal, hiredate " + 
					"	from emp where empno >= 7900" + 
					"	order by empno desc";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			if(rs != null ) {
				while(rs.next()) {

					int empno = rs.getInt("EMPNO");
					String ename = rs.getString("ENAME");
					double sal = rs.getDouble("SAL");
					Date hiredate = rs.getDate("HIREDATE");
					System.out.printf("%3d %s %7.2f %s \n", empno, ename, sal, hiredate);
				}
			}
		}catch(Exception e) {
			System.out.println("쿼리실행관련 에러발생 = " + e);
		}finally {
			try {
				if (pstmt != null) {pstmt.close();}
				if(conn != null) {conn.close();}
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
}

