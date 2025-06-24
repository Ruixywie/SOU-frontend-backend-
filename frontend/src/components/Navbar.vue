<template>
  <!-- 主页导航栏 -->
  <nav v-if="type === 'home'" class="navbar" :class="isScrolled ? 'non-transparent' : 'transparent'">
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
  <nav v-else class="navbar" :class="isScrolled ? 'non-transparent' : 'transparent'">
    <div class="navbar-container">
      <h1 class="navbar-title">SOU</h1>
      <ul class="navbar-menu">
        <li class="navbar-item"><a href="/"><img :src="'/icon/home.svg'" alt="icon" /></a></li>
        <li class="navbar-item"><a lang="zh" href="/login">登录</a></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, defineProps  } from 'vue';

const props = defineProps({
  type: {
    type: String,
    default: 'default'
  }
});

const isScrolled = ref(false);

// 定义滚动触发事件
function toggleNavbar() {
  isScrolled.value = window.scrollY > 100;
}

// 组件挂载时添加滚动事件监听
onMounted(() => {
  window.addEventListener('scroll', toggleNavbar);
});

// 组件卸载时移除滚动事件监听
onBeforeUnmount(() => {
  window.removeEventListener('scroll', toggleNavbar);
});
</script>

<style scoped>
.faded {
  opacity: 0;
}

.transparent {
  background-color: rgba(255, 255, 255, 0);
}

.non-transparent {
  /* background-color: rgb(255, 255, 255); */
  background-color: rgb(255, 255, 255, 0); /* 暂不实现透明度变化 */
}

.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  height: 60px;
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
  transition: .4s;
}

.navbar-item a {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #6f6f6f;
  transition: .4s;
}

.navbar-item a:hover {
  color: #000000;
}

.navbar-item a img {
  width: 30px;
  height: 30px;
  filter: invert(40%);
  transition: .4s;
}

.navbar-item a img:hover {
  filter: invert(0%);
}
</style>
