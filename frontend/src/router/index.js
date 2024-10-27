import { createRouter, createWebHistory } from 'vue-router'
import { ref } from 'vue';
// 从 views 文件夹中导入页面组件
import Home from '@/views/Home.vue'
import MyHomePage from '@/views/MyHomePage.vue';
import Articles from '@/views/Articles.vue';
import ArticleDetail from '@/views/ArticleDetail.vue';
import Login from '@/views/Login.vue';
import Fulilian from '@/views/Fulilian.vue';
import FulilianPictures from '@/views/FulilianPictures.vue';


const loading = ref(false); // 全局 loading 状态


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/my-home-page',
    name: 'MyHomePage',
    component: MyHomePage,
  },
  {
    path: '/articles',
    name: 'Articles',
    component: Articles,
  },
  {
    path: '/article',
    name: 'ArticleDetail',
    component: ArticleDetail, // 文章详情组件
    props: true // 允许将路由参数作为组件的 props
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/fulilian',
    name: 'Fulilian',
    component: Fulilian,
  },
  {
    path: '/fulilian/pictures',
    name: 'FulilianPictures',
    component: FulilianPictures,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// 全局路由守卫
router.beforeEach((to, from, next) => {
  loading.value = true; // 进入新页面时显示 Loader
  next();
});

router.afterEach(() => {
  setTimeout(() => {
    loading.value = false; // 加载完成，隐藏 Loader
  }, 500);
});

export { loading };
export default router;
