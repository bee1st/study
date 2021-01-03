<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import = "java.sql.*"%>
<%
	//DB연결
	Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid="root";
	String pw="1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
	
	//쿼리 생성
	String sql = "select * from practiceBoard order by id desc";
	
	//심부름꾼 생성
	Statement stmt = conn.createStatement();
	
	//쿼리 실행후 ResultSet으로
	ResultSet rs = stmt.executeQuery(sql);
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	td{
	border : 1px solid #cccccc
	}
</style>
</head>
<body>
<table width="900" align="center">
	<tr align="center">
		<td>제목</td>
		<td>이름</td>
		<td>조회수</td>
		<td>작성일</td>
	</tr>
<%
	while(rs.next())
	{
%>
	<tr>
		<td><a href="readnum.jsp?id=<%=rs.getString("id") %>"><%=rs.getString("title") %></a></td>
		<td align="center"><%=rs.getString("title") %></td>
		<td align="center"><%=rs.getString("readnum") %></td>
		<td align="center"><%=rs.getString("writeday") %></td>
	</tr>
<%
	}
%>
	<tr>
		<td colspan="4" align="center"><a href="write.jsp">글쓰기</a></td>
	</tr>

</table>
</body>
</html>
<%
	stmt.close();
	conn.close();
%>