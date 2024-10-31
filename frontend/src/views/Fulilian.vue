<template>
    <div class="fulilian">
        <!-- 背景 -->
        <div class="background" :style="{ backgroundImage: `url(${currentBackground})` }">
        </div>
        <div class="section">
            <!-- 轮播图 -->
            <div class="carousel-container">
                <Carousel :images="imageList" :autoPlayInterval="5000" @updateCurrentIndex="handleIndexUpdate" />
                <!-- 标题 -->
                <div class="title">
                    <h2>辛逝紀</h2>
                    <p class="current-time">{{ currentTime }}</p>
                </div>
            </div>
            <!-- 分类区 -->
            <div class="categories">
                <router-link :to="{ name: 'FulilianPictures' }" class="box" id="photos">
                    <h2>图集</h2>
                </router-link>
                <router-link :to="{ name: 'MyHomePage' }" class="box" id="videos">
                    <h2>视频集</h2>
                </router-link>
                <router-link :to="{ name: 'MyHomePage' }" class="box" id="links">
                    <h2>链接</h2>
                </router-link>
                <router-link :to="{ name: 'MyHomePage' }" class="box" id="comprehension">
                    <h2>综合</h2>
                </router-link>
            </div>
        </div>

    </div>
</template>


<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import Carousel from '@/components/Carousel.vue';

const currentTime = ref('');

import carouselPic1 from '@/assets/images/class/Fulilian/carousel/pic1.png';
import carouselPic2 from '@/assets/images/class/Fulilian/carousel/pic2.png';
import carouselPic3 from '@/assets/images/class/Fulilian/carousel/pic3.png';
import carouselPic4 from '@/assets/images/class/Fulilian/carousel/pic4.png';
import carouselPic5 from '@/assets/images/class/Fulilian/carousel/pic5.png';

const imageList = [
    carouselPic1,
    carouselPic2,
    carouselPic3,
    carouselPic4,
    carouselPic5
];

const currentIndex = ref(0);
const currentBackground = ref(imageList[0]); // 初始化背景图

// 监听 Carousel 组件发出的索引更新事件
const handleIndexUpdate = (index) => {
    currentIndex.value = index;
    currentBackground.value = imageList[index]; // 更新背景图
};

// 更新当前时间的函数
function updateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth() + 1; // 月份从0开始，所以要加1
    const day = now.getDate();
    const hour = now.getHours();
    const minute = now.getMinutes().toString().padStart(2, '0'); // 保证分钟是两位数
    const second = now.getSeconds().toString().padStart(2, '0'); // 保证秒是两位数

    // 生成日期和时间字符串
    currentTime.value = `${year}年${month}月${day}日${hour}:${minute}:${second}`; // 更新响应式属性
}

onMounted(() => {
    updateTime(); // 初始化时间
    const intervalId = setInterval(updateTime, 1000); // 每秒更新一次时间

    onBeforeUnmount(() => {
        clearInterval(intervalId); // 清除定时器
    });
});
</script>


<style scoped>
.fulilian {}

/* 背景 */
.background {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    filter: blur(5px);
    transition: background-image 1s ease;
    z-index: -1;
}

.section {
    padding-top: 60px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 200px;
}

.carousel-container {
    display: flex;
    gap: 60px;
    margin-top: 100px;
    width: 70%;
}

/* 标题 */
.title {
    width: 600px;
    position: relative;
    white-space: nowrap;
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-direction: column;
    text-shadow: 5px 5px 8px rgba(0, 0, 0, 0.8);
}

.title::before {
    width: 600px;
    height: 400px;
    content: '';
    position: absolute;
    top: -40px;
    right: -140px;
    background-image: url("@/assets/images/Fulilian/cover.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    mask-image:
        linear-gradient(to right, rgba(0, 0, 0, 0) 5%, rgba(0, 0, 0, 1) 80%),
        linear-gradient(to top, rgba(0, 0, 0, 0) 20%, rgba(0, 0, 0, 1) 80%);
    mask-composite: intersect;
    /* 合并两个渐变 */
    z-index: 1;
}

/* 标题 h2 */
.title h2 {
    font: 600 90px 'Kanaka-Font';
    color: #ffffff;
}

/* 标题 p */
.title p {
    font: 600 60px 'Kanaka-Font';
    color: #ffffff;
}

/* 分类区 */
.categories {
    max-width: 1000px;
    display: flex;
    gap: 50px;
    flex-wrap: wrap;
    /* 允许换行 */
    justify-content: center;
    align-items: center;
    margin-bottom: 60px;
}

.box {
    position: relative;
    border-radius: 10px;
    box-shadow: 0px 5px 8px rgba(0, 0, 0, 0.6);
    background-size: cover;
    background-position: 50% 50%;
    transition: .5s;
}

.box:hover {
    transform: translateY(-5px) scale(1.01);
    box-shadow: 0px 8px 10px rgba(0, 0, 0, 0.4);
}

.box h2 {
    position: absolute;
    left: 50%;
    bottom: 5%;
    transform: translateX(-50%);
    color: #ffffff;
    text-shadow: 0px 0px 5px black;
    letter-spacing: 2px;
    font: 100 28px '程荣光刻楷';
}

#photos {
    height: 250px;
    width: 250px;
    background-image: url("@/assets/images/Fulilian/categories/pic1.jpg");
}

#videos {
    height: 250px;
    width: 350px;
    background-image: url("@/assets/images/Fulilian/categories/pic2.jpg");
}

#links {
    height: 250px;
    width: 350px;
    background-image: url("@/assets/images/Fulilian/categories/pic3.jpg");
}

#comprehension {
    height: 250px;
    width: 250px;
    background-image: url("@/assets/images/Fulilian/categories/pic4.jpg");
}
</style>