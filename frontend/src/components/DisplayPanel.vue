<!-- DisplayPanel.vue -->
<template>
    <div class="display-panel">
        <div class="canvas" :style="{ backgroundImage: `url(${thumbnailUrl})` }"></div>
        <h2 class="display-name">{{ set.name }}</h2>
        <p class="set-description">{{ set.description }}</p>
        <a class="display-download-button" :href="downloadUrl" :download="set.name">
            <!-- 下载按钮图标 -->
            <svg t="1727246300741" class="icon" viewBox="0 0 1024 1024">
                <!-- SVG路径内容 -->
            </svg>
        </a>
    </div>
</template>

<script setup>
const props = defineProps({
    set: Object
});

// 生成展示图和下载图的 URL
const thumbnailUrl = `/static/${props.set.image_url.replace('original', 'thumbnail')}`;
const downloadUrl = `/static/${props.set.image_url}`;
</script>

<style scoped>
/* 展示面板 */
#display-panel {
    display: flex;
    position: fixed;
    transform: translate(-50%, -50%);
    top: 50%;
    left: 50%;
    gap: 40px;
    transition: .6s;
    z-index: 100;
}

/* 画布 */
.canvas {
    position: relative;
    width: 650px;
    height: 650px;
    background-color: #ebd2c5;
    border-radius: 8px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    border-top: solid 40px #ebd2c5;
    border-left: solid 30px #ebd2c5;
    border-right: solid 30px #ebd2c5;
    border-bottom: solid 80px #ebd2c5;
}

/* 切换按钮 */
.switch-button {
    width: 100%;
    height: 100%;
    position: absolute;
    display: flex;
    justify-content: space-between;
    user-select: none;
    /* 禁止文本选中 */
}

/* 左右按钮 */
.switch-left,
.switch-right {
    font-size: 50px;
    padding: 0;
    cursor: pointer;
    line-height: 550px;
    color: #000000;
}

/* 展示界面图片名称 */
.display-name {
    position: absolute;
    transform: translateX(-50%);
    left: 50%;
    bottom: -70px;
    font: 100 40px '优设标题黑';
    color: #ffffff;
    letter-spacing: 2px;
    text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.6);
    white-space: nowrap;
}

/* 展示界面下载链接 */
.display-download-button {
    width: 70px;
    height: 70px;
    padding: 15px;
    position: absolute;
    bottom: -70px;
    right: -10px;
    border-radius: 50%;
    background-color: rgb(70, 70, 70);
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle, rgba(0, 0, 0, 0.6) 0%, rgba(0, 0, 0, 0) 70%);
}

.display-download-button svg {
    width: 60px;
    height: 60px;
}

.display-download-button svg path {
    fill: #ffffff;
}

.notions {
    width: 750px;
    height: 650px;
    position: relative;
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
    border-radius: 8px;
    gap: 20px;
    overflow: hidden;
}

.set-description {
    position: relative;
    transform: translateX(-50%);
    left: 50%;
    margin-top: 30px;
    width: 600px;
    background-color: #f0f0f0;
    border-radius: 8px;
    border: solid 2px transparent;
    padding: 15px;
    transition: .2s;
    z-index: 1;
}

.set-description .description-content {
    font: 100 22px '优设标题黑';
    color: #000000;
    overflow: hidden;
    max-height: 30px;
    transition: max-height .2s ease-in-out;
    white-space: normal;
    /* 允许文本换行 */
    word-wrap: break-word;
    /* 允许长单词换行 */
    word-break: break-all;
    /* 在单词边界强制换行 */
}

.set-description:hover {
    border: solid 2px #000000;
}

.set-description:hover .description-content {
    max-height: none;
    /* 悬停时显示全部内容 */
}

.text-base {
    position: absolute;
    bottom: 0;
    height: 80px;
    width: 100%;
    background-color: #ffffff;
    padding: 20px;
    gap: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1;
}

.comment-input {
    width: 500px;
    padding: 12px 20px;
    border-radius: 30px;
    border: solid 2px transparent;
    background-color: #f0f0f0;
    font: 100 20px '优设标题黑';
    letter-spacing: 1px;
    margin-left: 40px;
    transition: .2s;
}

.comment-input:hover {
    border: solid 2px #aaaaaa;
}

.send-button {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    border-radius: 50%;
    background-color: #f0f0f0;
    border: none;
    cursor: pointer;
}

.send-button svg {
    width: 25px;
    height: 25px;
}

.send-button svg path {
    fill: #4c4c4c;
}

/* 留言部分 */
.content {
    position: relative;
    transform: translateX(-50%);
    left: 50%;
    height: 400px;
    width: 600px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: auto;
}

/* 留言 */
.comment {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    border-radius: 8px;
    background-color: #f6f6f6;
}

/* 头部 */
.head {
    display: flex;
    gap: 20px;
    align-items: center;
}

/* 头像 */
.head .ava {
    border-radius: 50%;
    background-color: #c1c1c1;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
}

/* 用户名 */
.head .user-name {
    font: 100 24px '优设标题黑';
    color: #000000;
}

/* 留言内容 */
.comment .word {
    margin-left: 70px;
    font: 100 22px '优设标题黑';
    color: #4f4f4f;
}

/* 留言部分占位符 */
.commentplaceholder {
    text-align: center;
    font: 100 36px '优设标题黑';
    color: #636363;
    margin-top: 50px;
}
</style>