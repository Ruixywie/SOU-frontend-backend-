<template>
    <div class="articles">
        <div class="article-section">
            <div class="masonry" id="masonry">
                <ArticleItem v-for="(article, index) in articles" :key="article.id" :article="article"
                    class="masonry-item" />
            </div>
            <!-- 侧边功能栏 -->
            <div class="article-function-bar">
                <FunctionBar :buttons="functionButtons" />
            </div>
        </div>

        <!-- Modal -->
        <Modal :visible="isModalVisible" @close="closeModal">
            <template v-if="modalType === 'uploadArticle'" #title>
                <div style="display: flex; flex-direction: column; justify-content: center; gap: 10px; margin-bottom: 20px;">
                    <label for="article-url" class="label">URL：</label>
                    <input v-model="articleUrl" type="text" id="article-url" class="input-field"
                        placeholder="输入文章URL..." />
                </div>
            </template>
            <template v-if="modalType === 'uploadArticle'" #content>
                <div style="display: flex; flex-direction: column; justify-content: center; gap: 10px; margin-bottom: 20px;">
                    <label for="article-title" class="label">当前文章标题：</label>
                    <input v-model="articleTitle" type="text" id="article-title" class="input-field"
                        placeholder="输入文章标题..." maxlength="25" />
                </div>
            </template>
            <template v-if="modalType === 'uploadArticle'" #footer>
                <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
                    <button class="confirmUploadArticle" @click="confirmUploadArticle">确认上传</button>
                </div>
            </template>
        </Modal>
    </div>
</template>

<script setup>
import ArticleItem from "@/components/ArticleItem.vue";
import { onMounted, ref } from "vue";
import axios from 'axios';
import FunctionBar from '@/components/FunctionBar.vue';
import imagesLoaded from "imagesloaded";
import Masonry from "masonry-layout";
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';

const { isModalVisible, modalType, openModal, closeModal } = useModal();

const articles = ref([]);  // 用于存储从后端获取的文章数据
const articleUrl = ref(''); // 文章URL
const articleTitle = ref(''); // 文章标题
const functionButtons = ref([
    {
        text: '上传',
        icon: '/icon/upload.svg',
        onClick: uploadArticle,
    },
]);

// 打开上传文章面板
function uploadArticle() {
    openModal('uploadArticle'); // 调用 useModal 中的 openModal
}

// 上传文章
const confirmUploadArticle = async () => {
  if (!articleUrl.value || !articleTitle.value) {
    alert("请填写所有必要信息");
    return;
  }

  // 创建 FormData 对象，用于发送URL和标题信息
  const formData = new FormData();
  formData.append('articleUrl', articleUrl.value);
  formData.append('articleTitle', articleTitle.value);

  try {
    // 发送 POST 请求上传文章
    const response = await axios.post('/api/upload_article_link', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    if (response.data.success) {
      alert('文章上传成功');
      // 清空表单
      articleUrl.value = '';
      articleTitle.value = '';
    }
  } catch (error) {
    console.error('文章上传失败:', error);
  }
};

// 页面加载时调用后端接口
const fetchArticles = async () => {
    try {
        const response = await fetch('/api/get_articles'); // 这里路径需匹配后端路由
        if (!response.ok) throw new Error('Network response was not ok');
        articles.value = await response.json();
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
};

onMounted(async () => {
    await fetchArticles(); // 确保文章加载后再初始化 Masonry
    imagesLoaded("#masonry", () => {
        new Masonry("#masonry", {
            itemSelector: ".masonry-item",
            columnWidth: ".masonry-item", //列宽
            gutter: 10, // 设置间距
            transitionDuration: '0.6s', // 设置过渡时间
            resize: true, // 窗口大小改变时重新布局
        });
    });
});
</script>

<style scoped>
.articles {
    padding-top: 60px;
    height: 100%;
}

.article-section {
    width: 100%;
    position: relative;
    padding: 20px 100px;
    /* 上下 左右 */
    z-index: 1;
    overflow: hidden;
}

.masonry {
    position: relative;
    width: 100%;
    min-width: 400px;
    height: auto;
}

.article-function-bar {
    position: fixed;
    width: 150px;
    right: 0;
    top: 50%;
    height: 50%;
    transform: translateY(-50%);
}

/* 标签 */
.label {
  font: 100 22px '程荣光刻楷';
  margin-top: 3px;
}

/* 输入框 */
.input-field {
  font: 100 18px '程荣光刻楷';
  border-radius: 4px;
  box-shadow: inset 1px 1px 2px rgba(0, 0, 0, 0.4), inset -1px -1px 2px rgba(255, 255, 255, 0.7);
  border: solid 1px #989898;
  letter-spacing: 1px;
  width: 500px;
  height: 35px;
  padding: 5px 10px;
  margin-left: 25px;
}

/* 确认上传按钮 */
.confirmUploadArticle {
  background-color: #0f68f7;
  padding: 10px 20px;
  font: 100 20px '程荣光刻楷';
  color: #fff;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  white-space: nowrap;
}
</style>