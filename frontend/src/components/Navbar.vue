<template>
  <!-- 主页导航栏 -->
  <nav v-if="type === 'home'" class="navbar">
    <div class="navbar-container">
      <h1 class="navbar-title">SOU</h1>
      <ul class="navbar-menu">
        <li class="navbar-item"><a href="https://github.com/Ruixywie/SOU-frontend-backend-"><img
              :src="'/icon/github-fill.svg'" alt="icon" /></a></li>
        <li class="navbar-item"><a href="https://www.youtube.com/"><img :src="'/icon/Youtube-fill.svg'"
              alt="icon" /></a></li>
        <li class="navbar-item"><a lang="zh" href="/about">关于</a></li>
      </ul>
    </div>
  </nav>
  <!-- 其他导航栏 -->
  <nav v-else class="navbar">
    <div class="navbar-container">
      <h1 class="navbar-title">SOU</h1>
      <ul class="navbar-menu">
        <li class="navbar-item"><a href="/"><img :src="'/icon/home-fill.svg'" alt="icon" /></a></li>
        <li class="navbar-item"><a lang="zh" href="/login">登录</a></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'default'
    }
  }
};
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  height: 60px;
  background-color: rgba(255, 255, 255, 0);
  z-index: 10;
  padding: 0 40px;
  transition: .4s;
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
  text-transform: uppercase;
  /* 将 logo 文本转为大写 */
  text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.8);
}

.navbar-menu {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  /* 水平方向上靠右对齐 */
  height: 100%;
  width: 50%;
  gap: 30px;
}

.navbar-item {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: .6s;
}

.navbar-item a {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #000000;
  text-shadow: 0px 0px 3px rgba(255, 255, 255, 1);
  transition: .6s;
}

.navbar-item a img {
  width: 30px;
  height: 30px;
}
</style>
