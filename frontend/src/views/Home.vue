<template>
  <div class="home">
    <div class="page-bg" ref="lottieContainer" id="top-animate"></div>
    <div class="page-bg" id="second-page-bg"></div>
    <div class='page-content' id="section1">
      <div :class="['titles', isHidden ? 'hide' : 'show']">
        <div class="title-abbreviation observe-fade">EmbraceU</div>
        <div class="title observe-fade">Embracing Universe</div>
        <div class="description observe-fade">Make Combination With Everything!</div>
      </div>
      <div class="buttons">
        <a id="show-documentation" class="button" lang="zh" @click="openModal('documentation')">重要公告</a>
        <router-link id="open-my-home-page" class="button" lang="zh" :to="{ name: 'MyHomePage' }">我的主页</router-link>
        <router-link id="open-articles-page" class="button" lang="zh" :to="{ name: 'Articles' }">文章</router-link>
        <router-link id="to-login" class="button" lang="zh" :to="{ name: 'Login' }">登录</router-link>
      </div>
    </div>
    <div class='page-content' id="section2">
      <div class="recommends">
        <router-link class="card" :to="{ name: 'Fulilian' }">
          <h2 lang="zh">葬送的芙莉莲</h2>
          <p lang="ja">葬送のフリーレン</p>
        </router-link>
        <a class="card" href="#">
          <h2 lang="zh">摄影</h2>
          <p>PHOTOS</p>
        </a>
        <a class="card" href="#">
          <h2 lang="zh">电影</h2>
          <p>FILMS</p>
        </a>
      </div>
    </div>

    <!-- Modal -->
    <Modal :visible="isModalVisible" @close="closeModal">
      <template v-if="modalType === 'documentation'" #title>
        <div style="margin-bottom: 20px;">
          <h2>SOU (Sharing Of Universe)</h2>
        </div>
      </template>
      <template v-if="modalType === 'documentation'" #subtitle>
        <div style="margin-bottom: 20px;">
          <p lang="zh">这是共享资源和快速搭建自己主页的网站，目前仍在开发阶段</p>
        </div>
      </template>
      <template v-if="modalType === 'documentation'" #content>
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <p lang="zh">目前已有的功能：</p>
          <li lang="zh">1、简单的注册和登录。（暂未实现验证码）</li>
          <li lang="zh">2、个人主页样例。（现有头像上传，名片展示，修改简介功能）</li>
          <li lang="zh">3、芙莉莲的图册部分资源分享页面（已经能够实现上传和下载，以及展示面板）</li>
          <li lang="zh">4、简单的评论区（已经实现按照用户发送评论）</li>
          <div style="height: 40px;"></div>
          <p lang="zh">前面的区域以后再来探索吧 !</p>
          <p>Peace!</p>
        </div>
      </template>
    </Modal>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';
import lottie from 'lottie-web'

const { isModalVisible, modalType, openModal, closeModal } = useModal();

const lottieContainer = ref(null)
let animationInstance = null

const currentPage = ref(0)

const bgElements = ref([])
const contentElements = ref([])

onMounted(() => {
  // 背景和内容分别收集
  bgElements.value = Array.from(document.querySelectorAll('.page-bg'))
  contentElements.value = Array.from(document.querySelectorAll('.page-content'))

  // 设置初始状态
  setActive(currentPage.value)

  const elements = document.querySelectorAll('.observe-fade');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        entry.target.classList.remove('fade-out');
      } else {
        entry.target.classList.remove('fade-in');
        entry.target.classList.add('fade-out');
      }
    });
  }, {
    threshold: 0.1
  });

  // 设置层次感：依次延迟显示
  elements.forEach((el, index) => {
    el.style.transitionDelay = `${index * 100}ms`; // 每个元素延迟 100ms
    observer.observe(el);
  });

  // 初始化 Lottie
  if (lottieContainer.value) {
    animationInstance = lottie.loadAnimation({
      container: lottieContainer.value,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: '/animations/top-animate.json',
    })
  }

  // 节流滚动触发（防抖节流控制滚动频率）
  let isScrolling = false
  const delay = 1000 // 每次切换需等待

  const handleScroll = (e) => {
    if (isScrolling) return

    const delta = e.deltaY
    isScrolling = true

    if (delta > 0 && currentPage.value < bgElements.value.length - 1) {
      currentPage.value++
    } else if (delta < 0 && currentPage.value > 0) {
      currentPage.value--
    }

    setActive(currentPage.value)

    setTimeout(() => {
      isScrolling = false
    }, delay)
  }

  window.addEventListener('wheel', handleScroll, { passive: false })
})

function setActive(index) {
  // 背景切换
  bgElements.value.forEach((el, i) => {
    el.classList.toggle('active', i === index)
  })

  // 内容切换
  contentElements.value.forEach((el, i) => {
    el.classList.toggle('active', i === index)
  })
}

onUnmounted(() => {
  // 取消观察
  const elements = document.querySelectorAll('.observe-fade')
  elements.forEach(el => observer?.unobserve(el))

  // 销毁动画
  if (animationInstance) {
    animationInstance.destroy()
  }
})
</script>

<style scoped>
/* home */
.home {
  height: 100%;
  width: 100%;
  background-color: #e6e5f2;
}

.page-bg, .page-content {
  opacity: 0;
  transition: opacity 0.8s ease;
  pointer-events: none; /* 防止鼠标交互冲突 */
}
.page-bg.active, .page-content.active {
  opacity: 1;
  pointer-events: auto;
}

#top-animate {
  position: fixed;
  top: -15%;
  left: 0;
  width: 110%;
  z-index: 1;
}

#section1 {
  border: solid 2px #000;
  transform: translateY(60px);
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 50px;
  width: 100%;
  /* height: 2000px; */
  padding-top: 50px;
  z-index: 2;
  /* display: none; */
}

/* 第二页背景图片 */
#second-page-bg {
  position: fixed;
  width: 100%;
  height: 100%;
  bottom: 0;
  right: 0;
  /* filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.2)); */
  background-image: url(@/assets/images/Home/secong-page-bg.png);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 1;
  /* border: solid 2px #000; */
}

#section2 {
  border: solid 2px #000;
  transform: translateY(60px);
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 50px;
  width: 100%;
  /* height: 2000px; */
  padding-top: 50px;
  z-index: 2;
  /* display: none; */
}

/* 左侧封面图片 */
.cover-image-left {
  position: fixed;
  width: 60%;
  height: 100%;
  top: 0;
  left: 0;
  background-image: url(@/assets/images/Home/home-background.png);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 1;
  mask-image: linear-gradient(to left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 30%);
  opacity: 0;
  /* 初始隐藏 */
  transition: opacity 0.8s ease;
}

/* title容器 */
.titles {
  display: flex;
  flex-direction: column;
  /* align-items: center; */
  justify-content: center;
  position: relative;
  width: 60%;
  transform: translateX(-20%);
  /* border: solid 2px #000; */
}

.observe-fade {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.6s ease-out;
}

.fade-in {
  opacity: 1;
  transform: translateY(0);
}

.fade-out {
  opacity: 0;
  transform: translateY(30px);
}

/* 缩略标题 */
.title-abbreviation {
  font-family: 'Italianno-Regular';
  font-size: 140px;
  color: #12d3e0;
  opacity: 0.3;
  letter-spacing: 4px;
  white-space: nowrap;
  /* border: solid 2px #000; */
}

/* 标题 */
.title {
  font-family: 'Italianno-Regular';
  font-size: 140px;
  opacity: 0.3;
  letter-spacing: 4px;
  white-space: nowrap;
  /* border: solid 2px #000; */
}

/* 简介 */
.description {
  margin-top: 40px;
  font-size: 30px;
  color: #8e8e8e;
  white-space: nowrap;
  /* border: solid 2px #000; */
}

/* 按钮容器 */
.buttons {
  display: flex;
  /* justify-content: center; */
  width: 60%;
  transform: translateX(-20%);
  gap: 30px;
  /* border: solid 2px #000; */
}

/* 按钮 */
.button {
  border-radius: 50px;
  padding: 12px 22px;
  font-size: 20px;
  border: none;
  cursor: pointer;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.25);
  white-space: nowrap;
}

#show-documentation {
  background-color: #d90a0a;
  color: #ffffff;
}

#open-my-home-page {
  background-color: #1551b1;
  color: #ffffff;
}

#to-login {
  background-color: #1551b1;
  color: #ffffff;
}

#open-articles-page {
  background-color: #1551b1;
  color: #ffffff;
}

/* 推荐链接容器 */
.recommends {
  display: flex;
  justify-content: center;
  width: 85%;
  display: flex;
  gap: 40px;
  /* border: solid 2px #000; */
}

/* 每个链接样式 */
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  border: solid 1px rgba(255, 255, 255, 0.2);
  width: 100%;
  min-width: 80px;
  max-width: 300px;
  height: 200px;
  padding: 10px 0px;
  border-radius: 24px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.25);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
  cursor: pointer;
  transition: .6s;
}

.card:nth-child(1) {
  background-image: url('@/assets/images/class/Fulilian/fulilian.png');
}

.card:nth-child(2) {
  background-image: url('@/assets/images/class/Photos/photo.png');
}

.card:nth-child(3) {
  background-image: url('@/assets/images/class/Films/film.png');
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.2);
}

.card h2 {
  width: 80%;
  position: relative;
  font-size: 24px;
  color: #ffffff;
  text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8);
  letter-spacing: .5px;
  -webkit-line-clamp: 1;
  display: -webkit-box;
  overflow: hidden;
  -webkit-box-orient: vertical;
}

.card p {
  width: 80%;
  position: relative;
  font-size: 14px;
  color: #ffffff;
  text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8);
  letter-spacing: .5px;
  -webkit-line-clamp: 1;
  display: -webkit-box;
  overflow: hidden;
  -webkit-box-orient: vertical;
}

.modal-container h2 {
  font-size: 30px;
}

.modal-container p {
  font-size: 24px;
}

.modal-container li {
  font-size: 22px;
  margin-left: 30px;
  color: #6c6c6c;
}
</style>
