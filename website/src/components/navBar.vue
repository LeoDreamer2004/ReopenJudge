<template>
  <nav class="navbar navbar-expand-md navbar-light" id="navbar">
    <a class="navbar-brand" href="/">ReopenJudge</a>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="/">首页</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/problems">题目清单</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/ide">在线IDE</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/algorithm">算法可视化</a>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <a class="nav-link" href="/register">注册</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/login">登录</a>
        </li>
      </ul>
      <!-- <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <span class="navbar-text no-dec" style="color:rgba(0,0,0,0.5); ">欢迎 &nbsp;</span>
        </li>
        <li class="nav-item">
          <div class="dropdown">
            <a class="drop-btn nav-link pr-3 pl-0" href="/profile" th:text="${user.name}"></a>
            <div class="dropdown-content" style="right: 0">
              <a href="/profile">个人主页</a>
              <a href="/admin" th:if="${user.isAdmin()}">站点管理</a>
              <a href="/logout">登出</a>
            </div>
          </div>
        </li>
      </ul> -->
    </div>
  </nav>
</template>

<script>
</script>

<style scoped>
#navbar {
  /* background-color: rgba(200, 230, 230, 0.5); */
  background-color: #e2f0fe;
  border: none;
  padding: 10px;
}
</style>
