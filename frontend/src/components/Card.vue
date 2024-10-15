<template>
  <div class="card">
    <div class="card-box" id="introduction">
      <div class="box-ring"></div>
      <div class="box-ring"></div>
      <h2>极简介</h2>
      <p>{{ introduction }}</p>
    </div>
    <div class="card-box" id="myname">
      <div class="box-ring"></div>
      <h2>{{ userName }}</h2>
    </div>
    <div class="card-box" id="tag">
      <div class="box-ring"></div>
      <div class="box-ring"></div>
      <h2>{{ tags.join(', ') }}</h2> <!-- 用于显示标签 -->
    </div>
    <img :src="avatar" id="avatar" alt="头像" />
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    introduction: {
      type: String,
      required: true,
    },
    userName: {
      type: String,
      required: true,
    },
    tags: {
      type: Array,
      default: () => [],
    },
    avatar: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
/* 名片 */
.card {
    width: 380px;
    height: 470px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 12px;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    transition: .8s;
    z-index: 2;
}
/* 名片三部分样式 */
.card .card-box {
    position: relative;
    width: 110%;
    height: 230px;
    background: linear-gradient(60deg, hsl(60, 100%, 90%), hsl(216, 100%, 70%));
    border-radius: 15px;
    box-shadow: 0px 8px 10px rgba(0, 0, 0, 0.6);
    transition: .8s;
}
.card .card-box:nth-child(2) {
    background: linear-gradient(60deg, hsl(60, 100%, 90%), hsl(177, 100%, 70%));
    height: 60px;
    width: 100%;
}
.card .card-box:nth-child(3) {
    background: linear-gradient(120deg, hsl(60, 100%, 90%), hsl(216, 100%, 70%));
    height: 200px;
    width: 100%;
    margin-left: 50px;
}
/* 头像 */
.card #avatar {
    position: absolute;
    top: 50%;
    left: -70px;
    transform: translateY(-50%);
    width: 220px;
    height: 220px;
    background: linear-gradient(60deg, #1b8e67, #8dfff4);
    border-radius: 50%;
    border: 18px solid #ffffff;
    object-fit: cover;
    transition: filter .5s;
    box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.2);
}
/* 头像 上方文字 */
.card #avatar::before {
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
    width: 150px;
    content: '更换头像';
    font: 100 30px '程荣光刻楷';
    position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%);
    color: #ffffff;
    transition: opacity .5s;
    opacity: 0;
    white-space: nowrap;
}
/* 卡片个人简介第一个泡泡 */
.card .card-box:nth-child(1) .box-ring:nth-child(1) {
    position: absolute;
    content: '';
    top: 50px;
    right: 35px;
    transform: translate(50%, -50%);
    width: 160px;
    height: 160px;
    border-radius: 50%;
    background: linear-gradient(70deg, hsl(216, 100%, 70%), hsl(163, 100%, 100%));
    /* 设置背景颜色 */
    transition: filter .5s;
    z-index: 1;
}
/* 卡片个人简介第一个泡泡 上方文字 */
.card .card-box:nth-child(1) .box-ring:nth-child(1):before {
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
    width: 100px;
    content: '详细简介';
    font: 100 20px '程荣光刻楷';
    position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%);
    color: #ffffff;
    transition: opacity .5s;
    opacity: 0;
}
/* 卡片个人简介第二个泡泡 */
.card .card-box:nth-child(1) .box-ring:nth-child(2) {
    position: absolute;
    content: '';
    top: 150px;
    right: 20px;
    transform: translate(50%, -50%);
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: linear-gradient(70deg, hsl(216, 100%, 70%), hsl(163, 100%, 100%));
    /* 设置背景颜色 */
    transition: filter .5s;
    z-index: 2;
}
/* 卡片个人简介第二个泡泡 上方文字 */
.card .card-box:nth-child(1) .box-ring:nth-child(2):before {
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
    width: 100px;
    content: '占位符';
    font: 100 18px '程荣光刻楷';
    position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%);
    color: #ffffff;
    transition: opacity .5s;
    opacity: 0;
}
/* 卡片名字第一个泡泡 */
.card .card-box:nth-child(2) .box-ring:nth-child(1) {
    position: absolute;
    content: '';
    top: 10px;
    right: 10px;
    transform: translate(50%, -50%);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: linear-gradient(60deg, hsl(177, 100%, 40%), hsl(163, 100%, 100%));
    /* 设置背景颜色 */
    transition: filter .5s;
    z-index: 1;
}
/* 卡片标签第一个泡泡 */
.card .card-box:nth-child(3) .box-ring:nth-child(1) {
    position: absolute;
    content: '';
    top: 150px;
    right: 90px;
    transform: translate(50%, -50%);
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: linear-gradient(120deg, hsl(216, 100%, 70%), hsl(163, 100%, 100%));
    /* 设置背景颜色 */
    transition: filter .5s;
    z-index: 2;
}
/* 卡片标签第二个泡泡 */
.card .card-box:nth-child(3) .box-ring:nth-child(2) {
    position: absolute;
    content: '';
    top: 130px;
    right: 20px;
    transform: translate(50%, -50%);
    width: 110px;
    height: 110px;
    border-radius: 50%;
    background: linear-gradient(120deg, hsl(216, 100%, 70%), hsl(163, 100%, 100%));
    /* 设置背景颜色 */
    transition: filter .5s;
    z-index: 1;
}
/* 卡片简介标题 */
.card #introduction h2 {
    font: 100 26px '程荣光刻楷';
    color: #124a5e;
    margin-left: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
    transition: .5s;
}
/* 卡片简介内容 */
.card #introduction p {
    font: 100 22px '程荣光刻楷';
    color: #124a5e;
    width: 250px;
    height: 85px;
    margin: 0px 60px 10px 55px;
    /* 上右下左 */
    transition: .5s;
    overflow: hidden;
}
/* 卡片名字文字 */
.card #myname h2 {
    font: 100 26px 'Montserrat-Regular';
    color: #124a5e;
    margin-left: 190px;
    margin-top: 10px;
    transition: .5s;
    white-space: nowrap;
}
/* 卡片标签标题 */
.card #tag h2 {
    font: 100 22px 'Montserrat-Regular';
    color: #124a5e;
    margin-left: 90px;
    margin-top: 25px;
    transition: .5s;
}
/* 卡片个人简介第一个泡泡鼠标悬停样式 */
.card .card-box:nth-child(1) .box-ring:nth-child(1):hover {
    filter: saturate(4) hue-rotate(50deg);
}
/* 卡片个人简介第一个泡泡 上方文字鼠标悬停样式 */
.card .card-box:nth-child(1) .box-ring:nth-child(1):hover:before {
    opacity: 1;
}
/* 卡片个人简介第二个泡泡鼠标悬停样式 */
.card .card-box:nth-child(1) .box-ring:nth-child(2):hover {
    filter: saturate(4) hue-rotate(50deg);
}
/* 卡片个人简介第二个泡泡 上方文字鼠标悬停样式 */
.card .card-box:nth-child(1) .box-ring:nth-child(2):hover:before {
    opacity: 1;
}
/* 卡片名字第一个泡泡鼠标悬停样式 */
.card .card-box:nth-child(2) .box-ring:nth-child(1):hover {
    filter: saturate(1.2) hue-rotate(-20deg);
}
/* 卡片标签第一个泡泡鼠标悬停样式 */
.card .card-box:nth-child(3) .box-ring:nth-child(1):hover {
    filter: saturate(4) hue-rotate(50deg);
}
/* 卡片标签第二个泡泡鼠标悬停样式 */
.card .card-box:nth-child(3) .box-ring:nth-child(2):hover {
    filter: saturate(4) hue-rotate(50deg);
}
/* 头像鼠标悬停样式 */
.card #avatar:hover {
    filter: saturate(1.2);
}
/* 头像 上方文字鼠标悬停样式 */
.card #avatar:hover:before {
    opacity: 1;
}
</style>
