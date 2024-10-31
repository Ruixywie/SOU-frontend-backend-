<template>
    <div class="myhomepage">
        <!-- 背景 -->
        <div class="background" :style="{ backgroundImage: `url(${background})`, filter: `blur(${backgroundBlur}px)` }">
        </div>
        <!-- title -->
        <div class="title" :style="{ opacity: titleOpacity }">
            <!-- 标题头像 -->
            <img class="title-img" :src="avatar">
            <!-- 标题文字 -->
            <h2>Ruixy</h2>
        </div>
        <!-- section -->
        <div class="section" :style="{ opacity: sectionOpacity }">
            <!-- 个人信息单元 -->
            <div class="individual-container">
                <!-- 个人简介 -->
                <UserProfile :avatar="avatar" :userName="userName" :introduction="introduction" />
                <!-- 侧边功能栏 -->
                <div class="individual-function-bar">
                    <FunctionBar :buttons="functionButtons" />
                </div>
            </div>
            <!-- 喜爱单元 -->
            <div class="favorite-unit">
                <LinkModule :modules="LinkModuleData" />
            </div>
        </div>

        <!-- Modal -->
        <Modal :visible="isModalVisible" @close="closeModal">
            <template v-if="modalType === 'editIntroduction'" #title>
                <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
                    <h2 style="font: 100 36px '程荣光刻楷';">修改个人简介</h2>
                </div>
            </template>
            <template v-if="modalType === 'editIntroduction'" #content>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <textarea v-model="newIntroduction" rows="5" cols="30"
                        style="width: 700px; height:450px; padding: 10px; font: 100 22px '程荣光刻楷'; color: #6e6e6e;"></textarea>
                </div>
            </template>
            <template v-if="modalType === 'editIntroduction'" #footer>
                <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
                    <button id="saveIntroduction" @click="saveIntroduction">保存</button>
                </div>
            </template>
        </Modal>

        <!-- 卡片模块 -->
        <div v-if="showCard">
            <Card :introduction="introduction" :userName="userName" :tags="tags" :avatar="avatar" />
        </div>

        <!-- ImageCropper 组件 -->
        <ImageCropper @upload="handleUpload" ref="imageCropper" />

    </div>
</template>


<script setup>
import { ref, onMounted, inject } from 'vue';
import axios from 'axios';
import UserProfile from '@/components/UserProfile.vue';
import FunctionBar from '@/components/FunctionBar.vue';
import Card from '@/components/Card.vue';
import ImageCropper from '@/components/ImageCropper.vue';
import LinkModule from '@/components/LinkModule.vue';
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';

const { isModalVisible, modalType, openModal, closeModal } = useModal();
const showNotification = inject('showNotification'); // 从全局注入 showNotification 方法

const userName = ref('Ruixy'); // 个人名称
const introduction = ref('这个人很懒，什么都没写'); // 个人简介
const avatar = ref('');  // 动态存储获取到的背景链接
const background = ref('');  // 动态存储获取到的头像链接
const tags = ref(['blender', 'ps']); // 标签
const newIntroduction = ref(''); // 用于临时存储用户输入的新简介
const showCard = ref(false); // 控制卡片显示
const imageCropper = ref(null); // 引用 ImageCropper 组件实例
const backgroundBlur = ref(0); // 初始模糊度
const sectionOpacity = ref(0); // 初始透明度
const titleOpacity = ref(1); // 初始透明度
const functionButtons = ref([
    {
        text: '卡片',
        icon: '/icon/id_card.svg',
        onClick: toggleCard,
    },
    {
        text: '更换',
        icon: '/icon/sync.svg',
        onClick: changeAvatar,
    },
    {
        text: '修改',
        icon: '/icon/edit-square.svg',
        onClick: openEditIntroductionModal,
    },
]);

import fulilianPoster from '@/assets/images/class/Fulilian/fulilian.png';
import fulilianIcon from '@/assets/images/class/Fulilian/fulilian-icon.png';
import photoPoster from '@/assets/images/class/Photos/photo.png';
import photoIcon from '@/assets/images/class/Photos/photo-icon.jpg';
import blenderPoster from '@/assets/images/class/Blender/blender.png';
import blenderIcon from '@/assets/images/class/Blender/blender-icon.png';
import filmPoster from '@/assets/images/class/Films/film.png';
import filmIcon from '@/assets/images/class/Films/film-icon.png';
const LinkModuleData = ref([
    { id: 1, title: '芙莉莲', subtitle: '猫猫', poster: fulilianPoster, icon: fulilianIcon, link: '/fulilian' },
    { id: 2, title: '我的照片', subtitle: '拍的照片', poster: photoPoster, icon: photoIcon, link: '#' },
    { id: 3, title: 'blender', subtitle: '开放世界', poster: blenderPoster, icon: blenderIcon, link: '#' },
    { id: 4, title: '电影', subtitle: '资源', poster: filmPoster, icon: filmIcon, link: '#' },
]);

// 请求后端avatar
import defaultAvatar from '@/assets/images/personal/default/avatar.png';
const getAvatar = async () => {
    try {
        // 这里请求 /get_avatar 路由，获取头像图片
        const response = await axios.get('/api/get_avatar', { responseType: 'blob' });
        // 使用 URL.createObjectURL 将 blob 转换为图片 URL
        avatar.value = URL.createObjectURL(response.data);
    } catch (error) {
        console.error('Error fetching avatar:', error);
        // 可以在这里设置默认头像
        avatar.value = defaultAvatar;
    }
};
// 请求后端background
import defaultBackground from '@/assets/images/personal/default/background.png';
const getBackground = async () => {
    try {
        // 这里请求 /background 路由，获取背景图片
        const response = await axios.get('/api/get_background', { responseType: 'blob' });
        // 使用 URL.createObjectURL 将 blob 转换为图片 URL
        background.value = URL.createObjectURL(response.data);
    } catch (error) {
        console.error('Error fetching background:', error);
        // 可以在这里设置默认头像
        background.value = defaultBackground;
    }
};

// 点击按钮时显示卡片
function toggleCard() {
    showCard.value = !showCard.value; // 切换卡片的显示状态
};
// 点击按钮更换头像
function changeAvatar() {
    imageCropper.value.triggerUpload(); // 调用子组件中的触发文件上传方法
};
// 处理裁剪后上传的图片
const handleUpload = async (croppedImageBlob) => {
    // 创建 FormData 对象
    const formData = new FormData();
    formData.append('file', croppedImageBlob, 'avatar.png'); // 添加文件数据到 FormData，'avatar.png' 为你希望发送的文件名

    try {
        const response = await fetch('/api/upload_avatar', {
            method: 'POST',
            body: formData, // 将 FormData 作为请求体
        });

        const data = await response.json(); // 解析响应
        if (data.status === 'success') {
            showNotification('头像上传成功'); // 处理上传成功的响应

            // 调用 getAvatar 函数以更新头像
            await getAvatar(); // 确保头像更新
        } else {
            showNotification('头像上传失败');
            console.error('头像上传失败', data.message); // 处理上传失败的响应
        }
    } catch (error) {
        showNotification('网络错误');
        console.error('网络错误', error); // 处理网络错误
    }
};
// 打开修改简介面板
function openEditIntroductionModal() {
    newIntroduction.value = introduction.value; // 将当前简介设置为新简介
    openModal('editIntroduction'); // 调用 useModal 中的 openModal
}
// 确认修改简介
const saveIntroduction = () => {
    introduction.value = newIntroduction.value; // 更新简介
    closeModal(); // 关闭模态框
};

// 鼠标滚动事件
const handleScroll = () => {
    const scrollY = window.scrollY; // 获取当前滚动距离
    // 当滚动距离大于 100px 时，添加模糊效果和显示 section
    if (scrollY > 100) {
        backgroundBlur.value = 10;
        sectionOpacity.value = 1;
        titleOpacity.value = 0;
    } else if (scrollY <= 100) {
        backgroundBlur.value = 0;
        sectionOpacity.value = 0;
        titleOpacity.value = 1;
    }
};

onMounted(() => {
    getAvatar();
    getBackground();
    window.addEventListener('scroll', handleScroll); // 监听滚动事件
});
</script>


<style scoped>
/* myhomepage */
.myhomepage {
    padding-top: 240px;
}

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
    transition: filter .6s;
    z-index: -1;
}

/* title */
.title {
    position: fixed;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    transform: translateX(-50%);
    left: 50%;
    bottom: 0;
    gap: 25px;
    opacity: 1;
    transition: opacity .6s;
    z-index: -1;
}

/* title 头像 */
.title-img {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    transform: translateY(-8px);
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.8), -.5px -.5px 2px white;
}

/* title 文字 */
.title h2 {
    font: 100 70px 'Italianno-Regular';
    color: #ffffff;
    text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.8), -.5px -.5px 2px white;
}

/* 内容部分 */
.section {
    width: 100%;
    min-width: 800px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 80px;
    gap: 30px;
    z-index: 1;
    background-color: rgba(244, 245, 247, 0);
    overflow: hidden;
    opacity: 0;
    transition: opacity .6s;
}

/* 个人信息单元 */
.individual-container {
    position: relative;
    width: 85%;
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
    gap: 40px;
    padding: 20px;
}

/* 修改简介按钮 */
#saveIntroduction {
    border-radius: 50px;
    padding: 12px 22px;
    font: 100 22px '程荣光刻楷';
    border: none;
    cursor: pointer;
    white-space: nowrap;
    background-color: #1551b1;
    color: #ffffff;
}

/* 个人信息侧边功能栏 */
.individual-function-bar {
    position: absolute;
    width: 150px;
    right: -130px;
    height: 90%;
}

/* 喜爱单元 */
.favorite-unit {
    position: relative;
    display: flex;
    justify-content: center;
    /* 在垂直方向上居中对齐子元素 */
    align-items: center;
    /* 在水平方向上居中对齐子元素 */
    gap: 60px;
    padding: 60px;
    margin-top: 300px;
}
</style>