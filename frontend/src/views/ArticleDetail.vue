<template>
    <div class="article-detail">
        <h1>{{ article.title }}</h1>
        <div id="editor" ref="editor"></div>
        <button @click="saveArticle">保存文章</button>
        <button @click="editArticle">编辑文章</button>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { useRoute } from 'vue-router';
import Quill from 'quill';
import 'quill/dist/quill.snow.css'; // 引入 Quill 样式

const route = useRoute();
const article = ref({}); // 用于存储文章数据
const editor = ref(null); // 用于存储 Quill 编辑器实例

// 获取文章详情
const fetchArticle = async () => {
    const articleId = route.query.p; // 获取查询参数
    try {
        const response = await fetch(`/api/get_article/${articleId}`); // 根据查询参数获取特定文章
        if (!response.ok) throw new Error('Network response was not ok');
        article.value = await response.json();
        nextTick(() => {
            // 在文章加载后设置编辑器的内容
            editor.value.setContents(editor.value.clipboard.convert(article.value.content));
        });
    } catch (error) {
        console.error('Error fetching article:', error);
    }
};

// 初始化 Quill 编辑器
const initEditor = () => {
    editor.value = new Quill('#editor', {
        theme: 'snow',
        modules: {
            toolbar: [
                ['bold', 'italic', 'underline'], // 字体样式
                ['link', 'image', 'video'], // 插入链接、图片、视频
                [{ list: 'ordered'}, { list: 'bullet' }], // 列表
                ['clean'] // 清除格式
            ]
        }
    });
};

// 保存文章
const saveArticle = async () => {
    const content = editor.value.root.innerHTML; // 获取编辑器内容
    const articleId = route.query.p; // 获取文章 ID
    try {
        const response = await fetch(`/api/update_article/${articleId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content }), // 发送内容
        });
        if (!response.ok) throw new Error('Network response was not ok');
        alert('文章保存成功!');
    } catch (error) {
        console.error('Error saving article:', error);
    }
};

// 编辑文章
const editArticle = () => {
    // 实现编辑文章的功能，例如显示编辑界面
};

onMounted(() => {
    fetchArticle(); // 获取文章内容
    initEditor(); // 初始化 Quill 编辑器
});
</script>

<style scoped>
.article-detail {
    padding-top: 60px;
}

#editor {
    height: 500px; /* 设置编辑器高度 */
    margin: 20px 0;
}

button {
    margin-right: 10px;
}
</style>
