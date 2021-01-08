<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>

<%
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@211.205.104.35:1521:xe";
	String uid = "ky";
	String upw = "1234";
	Class.forName(driver);
    Connection conn = DriverManager.getConnection(url, uid, upw);
	
	// request값
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id");
	String pager = request.getParameter("pager");
	String cla = request.getParameter("cla");
	String word = request.getParameter("word");
	//String name = session.getAttribute("userid").toString();
	
	//쿼리 생성
	String sql = "select * from fboard where id=" +id;
	
	//심부름꾼 생성
	Statement stmt = conn.createStatement();
	
	//쿼리 실행
	ResultSet rs = stmt.executeQuery(sql);
	rs.next();

%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	td {
	border:1px solid #cccccc;
	}
</style>
</head>
<body>
<table width="600" align="center">
<%@include file="header.jsp" %>
	<tr align="center">
		<td align="center">제목 </td>
		<td colspan="5"><%=rs.getString("title") %></td>
	</tr>
	<tr align="center">
		<td align="center"> 이름 </td>
		<td><%=rs.getString("name") %></td>
		<td align="center"> 작성일 </td>
		<td><%=rs.getString("writeday") %></td>
		<td align="center"> 조회수 </td>
		<td><%=rs.getString("readnum") %></td>	
	</tr>
	<tr>
	<tr height ="400">
		<td align="center"> 내용 </td>
		<td colspan="5"><%=rs.getString("content") %></td>
	</tr>
	<tr>
		<td colspan="6" align="center">
		<a href ="board_update.jsp?id=<%=rs.getInt("id")%>&pager=<%=pager%>&cla=<%=cla%>&word=<%=word%>">수정</a>
		<a href ="board_delete.jsp?id=<%=rs.getInt("id")%>"> 삭제</a>
		<a href ="board_list.jsp">목록보기</a></td>
	</tr>
</table>

</form>
<!-- 댓글관련 함수 추가 -->

<div align="center">
	<form id="dat" name="dat" method="post" action="board_dat_ok.jsp">
		<input type="hidden" name="dat_no_id" value="<%=id%>">
		<%=rs.getString("name") %>
		<input type="text" name="content" size="50" placeholder="댓글내용" id="content">
		<input type="submit" value="댓글달기" id="submit">
	</form>
</div>

<!-- 댓글 출력 -->
<%
	//DB 연결 => 위에서 이미 완료
	
	//쿼리 생성
	sql = "select * from fboard_dat where dat_no_id="+ id+ " ORDER BY dat_no DESC";
	
	//심부름꾼 생성 => 위에서 이미 완료
			
	//쿼리실행 후 => ResultSet
	rs = stmt.executeQuery(sql);

%>
<div align="center">
<table align="center" width="600">
	<%
		
		while(rs.next()) 
		{
			
	%>
	<tr>
		<td width="60"><%=rs.getString("name") %></td>
		<td><a href="javascript:board_mod('<%=rs.getString("dat_no")%>','<%=id %>')" id ="btn_dat_mod_<%=rs.getString("dat_no")%>"><%=rs.getString("content") %></a></td>
		<td><a href ="board_dat_delete.jsp?dat_no=<%=rs.getString("dat_no")%>&dat_no_id=<%=rs.getString("dat_no_id")%>"> X </a></td>
		<td width="100"><%=rs.getString("writeday") %></td>
	</tr>
	<%
		} 
	%>
</table>
<%@include file="footer.jsp" %>
</div>
<script>
IS_MOD = false;
function board_mod(dat_no, dat_no_id) {
	console.log(dat_no, dat_no_id);
	if(!IS_MOD)
	{
		
		var cts   = document.getElementById("btn_dat_mod_"+dat_no).innerHTML;
		var html1 = "<input id='input_dat_mod_"+dat_no+"' type='text' value='"+cts+"'><button onclick=\"mod_ok("+dat_no+","+dat_no_id+");\">수정</button>";
		document.getElementById("btn_dat_mod_"+dat_no).innerHTML = html1;
		
		console.log(html1);
		
		IS_MOD = true;
	}
	
}
function mod_ok(dat_no, dat_no_id) {
	var mod_cts = document.getElementById("input_dat_mod_"+dat_no).value;
	
	console.log(mod_cts);
	
	location.href = "board_dat_update.jsp?dat_no="+dat_no+"&content="+mod_cts+"&dat_no_id="+dat_no_id;
}
</script>
</body>
</html>
<%
	stmt.close();
	conn.close();
%>