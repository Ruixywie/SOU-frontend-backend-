<template>
  <div class="individual">
    <!-- 左侧头像和名字 -->
    <div class="individual-image">
      <img :src="avatar" class="my-img" alt="头像" />
      <div class="individual-name">
        <h2>{{ userName }}</h2>
      </div>
    </div>
    <!-- 右侧文字 -->
    <div class="introduction-text" lang="zh">
      <h2>个人简介</h2>
      <div class="brief-introduction-content">{{ introduction }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  props: {
    avatar: {
      type: String,
      required: true, // 确保传入头像链接
    },
    userName: {
      type: String,
      required: true, // 确保传入用户姓名
    },
    introduction: {
      type: String,
      required: true, // 确保传入个人简介
    },
  },
};
</script>

<style scoped>
/* 个人简介模块 */
.individual {
    position: relative;
    display: flex;
    width: 1100px;
    height: 500px;
    border-radius: 30px;
    box-shadow: 0px 8px 10px rgba(0, 0, 0, 0.6);
    transition: .8s;
    overflow: hidden;
    z-index: 1;
}
/* 个人简介模块鼠标悬停样式 */
.individual:hover {
    transform: scale(1.01);
}
.individual-image {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 60%;
    z-index: 1;
}
.my-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}
.introduction-text {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 60%;
    padding: 25px;
    padding-left: 125px;
    background-color: #ffffff;
    background: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 1) 20%); /* 渐变透明效果 */
    z-index: 2;
}
/* 个人简介模块的内容 */
.introduction-text h2 {
    font-size: 36px;
}
/* 个人简介模块内容 */
.brief-introduction-content {
    position: relative;
    margin: 20px 18px 20px 30px;
    /* 上右下左 */
    overflow: hidden;
    font-size: 26px;
    color: #6e6e6e;
}
/* 用户昵称 */
.individual-name {
    position: absolute;
    transform: translateX(-50%);
    left: 45%;
    bottom: 2%;
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
}
.individual-name h2 {
    font: 100 75px 'Italianno-Regular';
    color: #ffffff;
    text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.8), -.5px -.5px 2px white;
}
</style>
