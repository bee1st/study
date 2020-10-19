package jdbc;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SelectTest02 {

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
			String sql = "select mno, mname, mid, mpwd, mdate from member";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			if(rs != null ) {
				while(rs.next()) {
					MemberDTO mDTO = new MemberDTO();
					//여기에서는 member테이블의 mno컬럼의 값을 가져와서 
					//MemberDTO클래스의 setmNo()메서드 파라미터로 제공하면
					//MemberDTO클래스의 필드에 데이터가 세팅된다
					mDTO.setmNo(rs.getInt("MNO"));
					mDTO.setmName(rs.getString("mname"));
					mDTO.setmId(rs.getString("mid"));
					mDTO.setmPwd(rs.getString("mpwd"));
					mDTO.setmDate(rs.getDate("mdate"));
					System.out.println(mDTO.toString());
//					jdbc.MemberDTO@1efee8e7
//					jdbc.MemberDTO@1ee807c6
//					jdbc.MemberDTO@76a4d6c

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

