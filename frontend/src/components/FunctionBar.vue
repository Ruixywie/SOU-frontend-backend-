<template>
  <div class="function-bar">
    <button
      class="introduction-function"
      v-for="(button, index) in buttons"
      :key="index"
      @click="button.onClick"
    >
      <div class="sign">
        <img :src="button.icon" alt="icon" /> <!-- 根据传入的图标路径渲染图标 -->
      </div>
      <div class="sign-text">{{ button.text }}</div>
    </button>
  </div>
</template>

<script>
export default {
  name: 'FunctionBar',
  props: {
    buttons: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
/* 个人信息侧边功能栏 */
.function-bar {
    display: flex;
    flex-direction: column;
    gap: 20px;
    transition: .8s;
    align-items: center;
}
/* 功能按钮 */
.introduction-function {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 50px;
    height: 50px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    overflow: hidden;
    transition-duration: .3s;
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.25);
    background-color: #ffffff;
}
/* 图标 */
.sign {
    width: 100%;
    transition-duration: .3s;
    display: flex;
    align-items: center;
    justify-content: center;
}
.sign img {
    width: 25px;
}
/* 图标文字部分 */
.sign-text {
    position: absolute;
    right: 0%;
    width: 0%;
    opacity: 0;
    color: #4f4f4f;
    font-size: 1.5em;
    font-weight: 100;
    font-family: '程荣光刻楷';
    white-space: nowrap; /* 防止文本换行 */
    transition-duration: .3s;
}
/* 模块转卡片按钮鼠标悬停样式 */
.introduction-function:hover {
    width: 115px;
    border-radius: 40px;
    transition-duration: .3s;
}
.introduction-function:hover .sign {
    width: 45px;
    transition-duration: .3s;
    padding-left: 20px;
}
.introduction-function:hover .sign-text {
    opacity: 1;
    width: 70%;
    transition-duration: .3s;
    padding-right: 10px;
}
/* 点击效果*/
.introduction-function:active {
    transform: translate(2px, 2px);
}
</style>
