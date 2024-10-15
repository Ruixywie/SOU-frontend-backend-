<template>
    <div class="carousel-images">
        <!-- 图片 -->
        <ul class="pictures" :style="{ left: currentLeft + '%' }">
            <li v-for="(image, i) in images" :key="i" class="pic">
                <!-- 使用 <img> 标签显示图片 -->
                <img :src="image" alt="carousel image" />
            </li>
        </ul>
        <!-- 切换点 -->
        <ul class="dots">
            <li v-for="(image, i) in images" :key="i" class="dot" :class="{ active: i === currentIndex }"
                @click="goToSlide(i)"></li>
        </ul>
        <!-- 按钮 -->
        <div class="button">
            <div class="button-left" @click="prevSlide">&lt;</div>
            <div class="button-right" @click="nextSlide">&gt;</div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const props = defineProps({
    images: {
        type: Array,
        required: true
    },
    autoPlayInterval: {
        type: Number,
        default: 5000
    }
});

const emit = defineEmits(['updateCurrentIndex']);

const currentIndex = ref(0);
const currentLeft = ref(0); // 控制图片列表的偏移
let autoPlayTimer = null;

// 切换到下一张图片
const nextSlide = () => {
    currentIndex.value = (currentIndex.value + 1) % props.images.length;
    updatePosition();
    resetAutoPlay(); // 重新计时
};

// 切换到上一张图片
const prevSlide = () => {
    currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length;
    updatePosition();
    resetAutoPlay(); // 重新计时
};

// 根据索引跳转到指定的图片
const goToSlide = (index) => {
    currentIndex.value = index;
    updatePosition();
    resetAutoPlay(); // 重新计时
};

// 更新图片位置
const updatePosition = () => {
    currentLeft.value = currentIndex.value * -100;
    emit('updateCurrentIndex', currentIndex.value);
};

// 自动播放
const startAutoPlay = () => {
    autoPlayTimer = setInterval(() => {
        nextSlide();
    }, props.autoPlayInterval);
};

// 清除自动播放定时器
const stopAutoPlay = () => {
    if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
    }
};

// 重新计时
const resetAutoPlay = () => {
    stopAutoPlay();
    startAutoPlay();
};

onMounted(() => {
    startAutoPlay(); // 页面挂载后开始自动轮播
});

onBeforeUnmount(() => {
    stopAutoPlay(); // 页面销毁前清除定时器
});
</script>

<style scoped>
.carousel-images {
    position: relative;
    width: 400px;
    height: 400px;
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 5px 5px 8px rgba(0, 0, 0, 0.6), -1px -1px 2px white;
}

.pictures {
    display: flex;
    transition: left 0.5s ease-in-out;
    position: relative;
    width: 100%;
    height: 100%;
    left: 0;
}

.pic {
    list-style: none;
    flex-shrink: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pic img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}

.dots {
    display: flex;
    justify-content: center;
    position: absolute;
    bottom: 10px;
    left: 0;
    right: 0;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #ddd;
    margin: 0 5px;
    cursor: pointer;
}

.dot.active {
    background-color: #333;
}

.button {
    position: absolute;
    top: 50%;
    width: 100%;
    display: flex;
    justify-content: space-between;
    transform: translateY(-50%);
}

.button-left,
.button-right {
    cursor: pointer;
    padding: 20px;
    font-size: 40px;
    color: white;
    user-select: none;
}
</style>