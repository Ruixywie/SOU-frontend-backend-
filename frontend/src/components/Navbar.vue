<template>
  <nav class="navbar">
    <div class="navbar-container">
      <h1 class="navbar-title">SOU</h1>
      <ul class="navbar-menu">
        <li class="navbar-item"><a lang="zh" href="/">主页</a></li>
        <li class="navbar-item"><a lang="zh" href="/about">关于</a></li>
        <li class="navbar-item"><a lang="zh" href="/contact">联系</a></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  height: 60px;
  background-color: rgba(255, 255, 255, 0);
  z-index: 10;
  padding: 0 30px;
}
.navbar-container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.navbar-title {
  font-size: 30px;
  color: #000000;
  text-transform: uppercase; /* 将 logo 文本转为大写 */
  text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.8);
}
.navbar-menu {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* 水平方向上靠右对齐 */
  height: 100%;
  width: 50%;
  gap: 30px;
}
.navbar-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  width: 100px; /* 固定宽度 */
  border-radius: 30px;
  transition: .6s;
}
.navbar-item a {
  font-size: 22px;
  color: #000000;
  text-shadow: 0px 0px 3px rgba(255, 255, 255, 1);
  transition: .6s;
}
</style>
