<template>
    <div v-if="visible" class="notification" :class="{ show: visible }">
        {{ message }}
    </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue';

// 定义用于控制弹窗显示的状态和消息
const visible = ref(false);
const message = ref('');
let notificationTimeout = null;

// 方法：显示通知弹窗
const showNotification = (msg, duration = 3000) => {
    message.value = msg;
    visible.value = true;

    // 清除之前的定时器
    if (notificationTimeout) {
        clearTimeout(notificationTimeout);
    }

    // 设置新的定时器来隐藏通知
    notificationTimeout = setTimeout(() => {
        visible.value = false;
    }, duration);
};

// 组件卸载时清除定时器
onUnmounted(() => {
    if (notificationTimeout) {
        clearTimeout(notificationTimeout);
    }
});

// 暴露方法供外部使用
defineExpose({
    showNotification
});
</script>

<style scoped>
/* 通知弹窗 */
.notification {
    position: fixed;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    padding: 15px;
    margin: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    display: none;
    /* Hidden by default */
    font-size: 16px;
    max-width: 80%;
    text-align: center;
}

/* 控制通知弹窗显示 */
.notification.show {
    display: block;
}
</style>