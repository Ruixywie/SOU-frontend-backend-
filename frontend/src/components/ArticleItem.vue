<template>
    <article :id="`post-${articleData.id}`" class="masonry-item">
        <div class="masonry-inner">
            <div class="entry-top">
                <a :href="articleData.link" class="entry-thumbnail">
                    <img :src="articleData.thumbnail" :alt="articleData.title" />
                    <span class="thumb-icon"><i class="fas fa-star"></i></span>
                </a>
                <div class="entry-category">
                    <a :href="articleData.categoryLink" rel="category">{{ articleData.category }}</a>
                </div>
            </div>
            <h2 class="entry-title">
                <a :href="articleData.link" rel="bookmark">{{ articleData.title }}</a>
            </h2>
            <ul class="entry-meta">
                <li class="entry-date"><i class="far fa-calendar"></i> {{ articleData.date }}</li>
                <li class="entry-comments">
                    <a :href="`${articleData.link}#comments`">
                        <i class="far fa-comment"></i><span>{{ articleData.comments }} 评论</span>
                    </a>
                </li>
                <li class="entry-views"><span><i class="far fa-eye"></i> {{ articleData.views }} 次浏览</span></li>
            </ul>
        </div>
    </article>
</template>

<script setup>
import { computed } from "vue";
import { defineProps } from "vue";

const props = defineProps({
    article: {
        type: Object,
        required: true,
    },
});

import defaultThumbnail from '@/assets/images/article/image.png';
// 设置默认值
const articleData = computed(() => ({
    id: props.article.id || 0,
    link: props.article.link || '#',
    thumbnail: props.article.thumbnail || defaultThumbnail,
    title: props.article.title || 'Untitled Article',
    category: props.article.category || '暂未分类',
    categoryLink: props.article.categoryLink || '#',
    date: props.article.date || '未知时间',
    comments: props.article.comments ?? 0,
    views: props.article.views || '0',
}));
</script>

<style scoped>
/* 单个 article 外层容器 */
.masonry-item {
    width: 350px;
    background: #fff;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    margin: 15px;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.masonry-item:hover {
    transform: translateY(-3px);
}

/* 文章内容整体 */
.masonry-inner {
    padding: 16px;
}

/* 文章顶部，包含图片和分类 */
.entry-top {
    position: relative;
}

/* 文章图片 */
.entry-thumbnail {
    display: block;
    position: relative;
    overflow: hidden;
    border-radius: 8px;
}

.entry-thumbnail img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    transition: transform 0.3s ease;
}

.entry-thumbnail:hover img {
    transform: scale(1.05);
}

/* 图片右下角图标 */
.thumb-icon {
    position: absolute;
    bottom: 8px;
    right: 8px;
    background: rgba(0, 0, 0, 0.6);
    color: #fff;
    padding: 4px 8px;
    border-radius: 50%;
}

/* 分类标签 */
.entry-category {
    position: absolute;
    top: 8px;
    left: 8px;
    background: #ff6347;
    /* 可以选择一个醒目的颜色 */
    color: #fff;
    padding: 4px 8px;
    font-size: 12px;
    border-radius: 4px;
    text-transform: uppercase;
}

/* 文章标题 */
.entry-title {
    margin: 16px 0 8px;
    font-size: 1.25em;
    font-weight: bold;
}

.entry-title a {
    color: #333;
    text-decoration: none;
}

.entry-title a:hover {
    color: #ff6347;
}

/* 元数据部分（日期、评论、浏览量） */
.entry-meta {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    color: #888;
    font-size: 0.9em;
}

.entry-meta li {
    display: flex;
    align-items: center;
    gap: 4px;
}

.entry-meta i {
    color: #ff6347;
}
</style>