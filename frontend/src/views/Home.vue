<template>
  <div class="home">
    <!-- 当加载中时显示 Loader，完成后才显示内容 -->
    <Loader :visible="loading" />

    <!-- 当数据加载完成时才显示内容 -->
    <div class="section" v-if="!loading">
      <div class="title-abbreviation">SOU</div>
      <div class="title">Sharing Of Universe</div>
      <div class="description">Combine With Everything!</div>
      <img class="cover-image" src="@/assets/images/Home/cover.png">

      <div style="display: flex; gap: 30px; margin-top: 30px;">
        <a id="show-documentation" class="button" lang="zh" @click="openModal('documentation')">重要公告</a>
        <router-link id="open-my-home-page" class="button" lang="zh" :to="{ name: 'MyHomePage' }">我的主页</router-link>
        <router-link id="open-articles-page" class="button" lang="zh" :to="{ name: 'Articles' }">文章</router-link>
        <router-link id="to-login" class="button" lang="zh" :to="{ name: 'Login' }">登录</router-link>
      </div>
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
import { ref, onMounted } from 'vue';
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';
import Loader from '@/components/Loader.vue'

const { isModalVisible, modalType, openModal, closeModal } = useModal();
const loading = ref(true)

onMounted(async () => {
  loading.value = false // 加载完成后隐藏 Loader
})
</script>

<style scoped>
/* home */
.home {
  height: 100%;
  background-color: #eeeeee;
}

.section {
  transform: translateY(70px);
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 5px;
  width: 100%;
  padding: 50px 260px 0px 260px;
}

/* 缩略标题 */
.title-abbreviation {
  font-size: 60px;
  color: #12d3e0;
  white-space: nowrap;
}

/* 标题 */
.title {
  font-size: 60px;
  white-space: nowrap;
}

/* 简介 */
.description {
  margin-top: 10px;
  font-size: 30px;
  color: #8e8e8e;
  white-space: nowrap;
}

/* 封面图片 */
.cover-image {
  position: absolute;
  width: 300px;
  top: 40px;
  right: 260px;
  filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.2));
  z-index: -1;
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
  width: 100%;
  display: flex;
  gap: 40px;
  margin-top: 30px;
  padding: 20px;
}

/* 每个链接样式 */
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-end;
  border: solid 1px rgba(255, 255, 255, 0.2);
  width: 300px;
  height: 200px;
  min-width: 300px;
  min-height: 200px;
  padding: 10px 20px;
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
  right: 0;
  bottom: 10px;
  font-size: 24px;
  color: #ffffff;
  text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8);
  letter-spacing: .5px;
  white-space: nowrap;
}

.card p {
  right: 0;
  bottom: 0;
  font-size: 14px;
  color: #ffffff;
  text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8);
  letter-spacing: .5px;
  white-space: nowrap;
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
