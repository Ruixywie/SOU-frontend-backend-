<!-- DisplayPanel.vue -->
<template>
    <!-- 遮罩层 -->
    <div class="overlay"></div>

    <div class="display-panel">
        <!-- 关闭按钮 -->
        <span class="close-button" @click="closePanel">&times;</span>

        <div class="canvas">
            <!-- 显示图片 -->
            <img v-if="set.imageBlobUrl" class="image" :src="set.imageBlobUrl" />
            <div class="display-name">{{ set.name }}</div>

            <!-- 切换按钮 -->
            <div class="switch-button">
                <div class="switch-left" @click="switchSet('left')">&lt;</div>
                <div class="switch-right" @click="switchSet('right')">&gt;</div>
            </div>
            <a class="display-download-button" :href="set.imageBlobUrl" :download="set.name">
                <!-- 下载按钮图标 -->
                <svg t="1727246300741" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="8495">
                    <path
                        d="M505.7 661c3.2 4.1 9.4 4.1 12.6 0l112-141.7c4.1-5.2 0.4-12.9-6.3-12.9h-74.1V168c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v338.3H400c-6.7 0-10.4 7.7-6.3 12.9l112 141.8z"
                        p-id="8496"></path>
                    <path
                        d="M878 626h-60c-4.4 0-8 3.6-8 8v154H214V634c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v198c0 17.7 14.3 32 32 32h684c17.7 0 32-14.3 32-32V634c0-4.4-3.6-8-8-8z"
                        p-id="8497"></path>
                </svg>
            </a>
        </div>

        <div class="notions">
            <!-- 描述部分 -->
            <div class="set-description">
                <div class="description-content">{{ set.description }}</div>
            </div>

            <!-- 留言部分 -->
            <div class="content" id="comment-section">
                <!-- 遍历评论 -->
                <div v-for="(comment, index) in set.comments" :key="index" class="comment">
                    <div class="head">
                        <div class="ava">
                            <img :src="comment.avatar" alt="avatar" />
                        </div>
                        <div class="user-name">{{ comment.username }}</div>
                    </div>
                    <div class="word">{{ comment.comment }}</div>
                </div>
            </div>

            <!-- 输入部分 -->
            <div class="text-base">
                <!-- 输入框 -->
                <input v-model="newComment" type="text" class="comment-input" placeholder="输入文字..." />
                <!-- 发送按钮 -->
                <button class="send-button" @click="sendComment">
                    <svg t="1727447306870" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="8495" width="200" height="200">
                        <path
                            d="M868 545.5L536.1 163c-12.7-14.7-35.5-14.7-48.3 0L156 545.5c-4.5 5.2-0.8 13.2 6 13.2h81c4.6 0 9-2 12.1-5.5L474 300.9V864c0 4.4 3.6 8 8 8h60c4.4 0 8-3.6 8-8V300.9l218.9 252.3c3 3.5 7.4 5.5 12.1 5.5h81c6.8 0 10.5-8 6-13.2z"
                            p-id="8496"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const props = defineProps({
    set: Object
});

const emit = defineEmits(['close', 'switchSet']);
const newComment = ref(''); // 新增的 v-model 绑定的评论内容

// 触发关闭事件
const closePanel = () => {
    emit('close');
};

// 切换图片
const switchSet = (direction) => {
    emit('switchSet', direction);
};

// 发送评论
const sendComment = async () => {
    if (!newComment.value) {
        alert('请输入评论内容');
        return;
    }

    try {
        const response = await axios.post('/api/add_comment', {
            image_id: props.set.id,
            comment: newComment.value
        });

        if (response.data.success) {
            // 添加新评论到当前图片集的评论列表
            props.set.comments.push({
                username: '默认用户名',  // 暂时用默认用户名
                avatar: '/path/to/default-avatar.jpg',  // 暂时用默认头像
                comment: newComment.value
            });

            // 清空输入框
            newComment.value = '';
        } else {
            console.error('Failed to add comment:', response.data.error);
        }
    } catch (error) {
        console.error('Error submitting comment:', error);
    }
};
</script>

<style scoped>
/* 设置遮罩层 */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    /* 半透明黑色遮罩 */
    z-index: 9998;
}

/* 展示面板 */
.display-panel {
    display: flex;
    position: fixed;
    transform: translate(-50%, -50%);
    top: 50%;
    left: 50%;
    gap: 40px;
    transition: .6s;
    z-index: 9999;
}

/* 关闭按钮样式 */
.close-button {
    position: absolute;
    top: 2%;
    right: 2%;
    border: none;
    cursor: pointer;
    font-size: 38px;
    z-index: 10000;
}

/* 画布 */
.canvas {
    position: relative;
    width: 650px;
    height: 650px;
    background-color: #ebd2c5;
    border-radius: 8px;
    border-top: solid 40px #ebd2c5;
    border-left: solid 30px #ebd2c5;
    border-right: solid 30px #ebd2c5;
    border-bottom: solid 80px #ebd2c5;
}

.image {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

/* 切换按钮 */
.switch-button {
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
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
    font: 100 40px '程荣光刻楷';
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
    font: 100 22px '程荣光刻楷';
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
    font: 100 20px '程荣光刻楷';
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
    overflow: hidden;
}

.head .ava img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* 用户名 */
.head .user-name {
    font: 600 24px 'Montserrat-Regular';
    color: #000000;
}

/* 留言内容 */
.comment .word {
    margin-left: 70px;
    font: 100 22px '程荣光刻楷';
    color: #4f4f4f;
}

/* 留言部分占位符 */
.commentplaceholder {
    text-align: center;
    font: 100 36px '程荣光刻楷';
    color: #636363;
    margin-top: 50px;
}
</style>