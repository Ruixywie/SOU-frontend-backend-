<template>
  <div id="app">
    <Loader :visible="loading" /> <!-- 当加载中时显示 Loader，完成后才显示内容 -->
    <Navbar /> <!-- 添加导航栏 -->
    <Notification ref="notification" /> <!-- 添加通知弹窗 -->
    <router-view v-if="!loading" /> <!-- 动态渲染匹配的路由组件 -->
  </div>
</template>

<script setup>
import { ref, provide, onMounted } from 'vue';
import Loader from '@/components/Loader.vue';
import { loading } from '@/router'; // 导入全局 loading 状态
import Navbar from '@/components/Navbar.vue'
import Notification from '@/components/Notification.vue';

const notification = ref(null); // 创建 notification 引用

// 提供全局 showNotification 方法，供所有子组件调用
provide('showNotification', (message, duration = 3000) => {
  notification.value.showNotification(message, duration);
});
</script>

<style></style>
