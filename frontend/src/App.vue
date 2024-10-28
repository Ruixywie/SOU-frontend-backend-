<template>
  <div id="app">
    <Loader :visible="loading" /> <!-- 当加载中时显示 Loader，完成后才显示内容 -->
    <Navbar :type="navbarType" /> <!-- 添加导航栏 -->
    <Notification ref="notification" /> <!-- 添加通知弹窗 -->
    <router-view v-if="!loading" /> <!-- 动态渲染匹配的路由组件 -->
  </div>
</template>

<script setup>
import { ref, provide, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import Loader from '@/components/Loader.vue';
import { loading } from '@/router'; // 导入全局 loading 状态
import Navbar from '@/components/Navbar.vue'
import Notification from '@/components/Notification.vue';

const route = useRoute(); // 获取当前路由
const notification = ref(null); // 创建 notification 引用

// 动态计算 navbarType，基于当前路由的 meta 字段
const navbarType = computed(() => route.meta.navbarType || 'default');

// 提供全局 showNotification 方法，供所有子组件调用
provide('showNotification', (message, duration = 3000) => {
  notification.value.showNotification(message, duration);
});
</script>

<style></style>
