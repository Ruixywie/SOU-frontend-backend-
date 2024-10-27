<template>
    <div class="articles">
        <div class="article-section">
            <div class="masonry" id="masonry">
                <ArticleItem v-for="(article, index) in articles" :key="article.id" :article="article"
                    class="masonry-item" />
            </div>
        </div>
    </div>
</template>

<script setup>
import ArticleItem from "@/components/ArticleItem.vue";
import { onMounted, ref } from "vue";
import imagesLoaded from "imagesloaded";
import Masonry from "masonry-layout";

const articles = ref([]);  // 用于存储从后端获取的文章数据



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
</style>