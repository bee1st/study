<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="java.sql.*"%>
<%@	page import="pro_fboard.dto.FboardDto"%>
<%@	page import="pro_fboard.dao.FboardDao"%>
<%
	int id = Integer.parseInt(request.getParameter("id"));
	FboardDao fdao = new FboardDao();
	FboardDto fdto = fdao.content(id);
	session.setAttribute("userid", "user1");
	
	String userid = session.getAttribute("userid").toString();
	String pager = request.getParameter("pager");
	String cla = request.getParameter("cla");
	String word = request.getParameter("word");
%>
<jsp:include page="/header.jsp" />
<section id="fboard_update">
	<div class="container">
		<div class="row">
			<div class="fboard_update">
				<form method="post" action="board_update_ok.jsp">
					<input type="hidden" name="id" value="<%=id%>"> <input
						type="hidden" name="pager" value="<%=pager%>"> <input
						type="hidden" name="cla" value="<%=cla%>"> <input
						type="hidden" name="word" value="<%=word%>">
					<table width="600" align="center">
						<tr>
							<td>제목</td>
							<td colspan="6"><input type="text" name="title"></td>
						</tr>
						<tr>
							<td align="center">이름</td>
							<td><%=fdto.getUserid()%></td>
							<td align="center">작성일</td>
							<td><%=fdto.getWriteday()%></td>
							<td align="center">조회수</td>
							<td><%=fdto.getReadnum()%></td>
						</tr>
					</table>
					<table width="600" align="center">
						<tr>
							<td height="400"><textarea cols="80" rows="30"
									name="content"></textarea></td>
						</tr>
						<tr>
							<td colspan="2" align="center"><input type="submit"
								value="수정하기"></td>
						</tr>
					</table>
				</form>

			</div>
		</div>
	</div>
</section>
<jsp:include page="footer.jsp" />