<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@	page import="java.util.ArrayList" %>
<%@	page import="pro_fboard.dto.FboardDto" %>
<%@	page import="pro_fboard.dao.FboardDao" %>

<%
	String userid = (String)session.getAttribute("userid");
	request.setCharacterEncoding("utf-8");
    String pager = request.getParameter("pager");
    FboardDto fdto = new FboardDto();
    FboardDao fdao = new FboardDao();
    
    String cla = request.getParameter("cla");
    String word = request.getParameter("word");
    ArrayList<FboardDto> list = fdao.list(cla, word, pager);
    /* 
    create table fboard
	(
		id number(8),
		title varchar(40),
		name varchar(20),
		content varchar(2000),
		readnum number(8) default 0,
		writeday date);
    
	기본키 지정
    alter table fboard add constraint fboard_pk primary key (id);
	시퀀스 생성
    create sequence fboard_seq start with 1 increment by 1 maxvalue 1000000 nocycle; */
    
    
%>   
<jsp:include page="header.jsp" />
<section id="sec_fboardlist">
	<div class="container">
		<div class="row">
		<div class="div_fboardlist">
<div align="center">

	<form name="searchFrm" method="post" action="board_list.jsp">
		<select name="cla">
			<option value="name">이름</option>
			<option value="title">제목</option>
		</select>
		<input type="text" name="word" value="<%=word%>">
		<input type="submit" value="검색">
	</form>
</div>


<table>

	<tr align="center">
		<td> 번호 </td>
		<td> 제목 </td>
		<td> 이름 </td>
		<td> 조회수 </td>
		<td> 등록일 </td>
	</tr>
<%
	for(int i = 0; i < list.size(); i++)
	{
%>
	<tr>
		<td align="center"><%=fdto.getId() %></td>
		<td><a href="board_readnum.jsp?id=<%=fdto.getId()%>&pager=<%=pager%>&cla=<%=cla%>&word=<%=word%>"><%=fdto.getTitle() %></a></td>
		<td align="center"><%=fdto.getUserid()%></td>
		<td align="center"><%=fdto.getReadnum() %></td>
		<td align="center"><%=fdto.getWriteday() %></td>
	</tr>
<%
	}
%>
		<!-- 사용자가 클릭하여 이동할 수 있는 페이지 출력 -->
		<tr>
			<td colspan="4" align="center">
			<%
				//총 페이지 값을 구하기 => 총 레코드수/ 페이지당 레코드수
				int page_cnt = fdao.get_total_page_cnt();
				int pstart = fdao.get_page_start(pager);
				int pend =fdao.get_page_end(pager, page_cnt);
			
				if(page_cnt < pend){
					pend = page_cnt;
				}
			%>
			<!--10페이지 이전 페이지 이동  -->
			<%if(pstart != 1)
			{ 
			%>
			<a href="board_list.jsp?pager=<%=pstart-1%>&cla=<%=cla%>&word=<%=word%>">&#60;&#60;</a>
			<%} else{%>
				&#60;&#60;
			<%} %>
			
			<!-- 1페이지 이전 페이지 이동-->
			<%if(Integer.parseInt(pager) != 1){ %>
				<a href="board_list.jsp?pager=<%=Integer.parseInt(pager)-1%>&cla=<%=cla%>&word=<%=word%>">&#60;</a>
			<%} else{%>
				&#60;
			<%} %>
			
			<!-- pstart ~ pend 페이지출력 현재페이지는 색 변경 -->
			<%  
				for(int i= pstart; i<=pend; i++){
					String str = "";
					if(Integer.parseInt(pager) == i) str="style='color:red;'";
			%>
				<a href="board_list.jsp?pager=<%=i%>&cla=<%=cla%>&word=<%=word%>" <%=str%>><%=i %></a>
			<%} %>
			
			<!-- 1페이지 이후 페이지 이동-->
			<%if(Integer.parseInt(pager) != page_cnt){ %>
				<a href="board_list.jsp?pager=<%=pager+1%>&cla=<%=cla%>&word=<%=word%>">&#62;</a>
			<%} else{%>
				&#62;
			<%} %>
			
			<!--10페이지 이후 페이지 이동  -->
			<%if(pend != page_cnt){ %>
				<a href="board_list.jsp?pager=<%=pend+1%>&cla=<%=cla%>&word=<%=word%>">&#62;&#62;</a>
			<%} else{%>
				&#62;&#62;
			<%} %>
			</td>
		</tr>
		<tr>
			<td colspan="2" align="center"><a href="board_write.jsp">글쓰기</a></td>
			<td colspan="2" align="center"><a href="board_list.jsp">목록보기</a></td>
	</table>
	</div>
		</div>
	</div>
</section>
<script>
	function init(){
		document.searchFrm.cla.value="<%=cla%>"
	}
</script>
<jsp:include page="footer.jsp" />
