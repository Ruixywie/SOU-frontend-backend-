import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import VueLazyload from 'vue-lazyload'; // 引入 vue-lazyload 插件

// 引入全局样式
import '@/assets/styles/global.css'

const app = createApp(App);

import errorImage from '@/assets/images/sets/error.png';
import loadingImage from '@/assets/images/sets/loading.gif';

// 配置 vue-lazyload
app.use(VueLazyload, {
  preLoad: 1.2,  // 提前加载的比例
  error: errorImage, // 加载失败时显示的图片路径
  loading: loadingImage, // 加载时显示的占位图片路径
  attempt: 1, // 加载失败时的重试次数
});

// 使用 router
app.use(router);
app.mount('#app');
