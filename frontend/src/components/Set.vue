<!-- Set.vue -->
<template>
    <div class="set" @click="showDetails">
        <!-- 使用 <img> 标签展示压缩的图片 -->
        <img v-if="compressedImageBlobUrl" :src="compressedImageBlobUrl" alt="Thumbnail" class="thumbnail-image" />

        <!-- 下载按钮 -->
        <a class="download-button" :href="imageBlobUrl" :download="setData.name" @click.stop.prevent="downloadImage">
            <!-- 下载按钮图标 -->
            <svg t="1727246300741" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="8495">
                <path
                    d="M505.7 661c3.2 4.1 9.4 4.1 12.6 0l112-141.7c4.1-5.2 0.4-12.9-6.3-12.9h-74.1V168c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v338.3H400c-6.7 0-10.4 7.7-6.3 12.9l112 141.8z"
                    p-id="8496"></path>
                <path
                    d="M878 626h-60c-4.4 0-8 3.6-8 8v154H214V634c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v198c0 17.7 14.3 32 32 32h684c17.7 0 32-14.3 32-32V634c0-4.4-3.6-8-8-8z"
                    p-id="8497"></path>
            </svg>
        </a>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
const props = defineProps({
    setData: Object
});

const imageBlobUrl = computed(() => props.setData.imageBlobUrl); // 获取原始图片下载链接
const compressedImageBlobUrl = ref(null);  // 存储压缩后的图片URL

// 使用 Canvas 压缩图片
const compressImage = (img) => {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const maxWidth = 1024;  // 压缩后的最大宽度
    const maxHeight = 1024; // 压缩后的最大高度
    let width = img.width;
    let height = img.height;

    // 计算压缩后的尺寸
    if (width > height) {
        if (width > maxWidth) {
            height = Math.round((height *= maxWidth / width));
            width = maxWidth;
        }
    } else {
        if (height > maxHeight) {
            width = Math.round((width *= maxHeight / height));
            height = maxHeight;
        }
    }

    // 设置 Canvas 大小并绘制图像
    canvas.width = width;
    canvas.height = height;
    ctx.drawImage(img, 0, 0, width, height);

    // 将压缩的图片转换为 Blob URL
    canvas.toBlob((blob) => {
        compressedImageBlobUrl.value = URL.createObjectURL(blob);
    }, 'image/png');
};

// 触发父组件的展示详情事件
const emit = defineEmits(['showDetails']);
const showDetails = () => {
    // 传递 setData，并传递压缩后的图片 URL
    emit('showDetails', {
        ...props.setData,
        compressedImageBlobUrl: compressedImageBlobUrl.value
    });
};

// 下载图片
const downloadImage = () => {
    const link = document.createElement('a');
    link.href = imageBlobUrl.value;
    link.download = props.setData.name;
    link.click();
};

// 加载图片并压缩
onMounted(() => {
    const img = new Image();
    img.src = imageBlobUrl.value;
    img.onload = () => compressImage(img);
});

// 清理 Blob URL
onUnmounted(() => {
    if (compressedImageBlobUrl.value) {
        URL.revokeObjectURL(compressedImageBlobUrl.value);
    }
    if (imageBlobUrl.value) {
        URL.revokeObjectURL(imageBlobUrl.value);
    }
});
</script>

<style scoped>
/* 图片单元 */
.set {
    width: 300px;
    height: 350px;
    border-radius: 5px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-color: #fad7c4;
    box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.25);
    cursor: pointer;
    overflow: hidden;
    transition: .8s;
}

.set:hover {
    transform: scale(1.02);
}

.thumbnail-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* 下载按钮 */
.download-button {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 90px;
    height: 90px;
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    padding: 10px;
    text-decoration: none;
    opacity: 0;
    /* 初始不可见 */
    transform: translate(2px, 2px);
    transition: 0.5s ease;
    background: linear-gradient(to bottom right, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.6) 110%);
}

.download-button svg {
    width: 30px;
    height: 30px;
}

.download-button svg path {
    fill: #ffffff;
}

.set:hover .download-button {
    opacity: 1;
    /* 变得可见 */
    transform: translate(0px, 0px);
}
</style>