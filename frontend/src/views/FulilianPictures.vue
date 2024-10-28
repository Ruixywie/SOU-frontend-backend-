<template>
  <div class="fulilianpicture">
    <!-- 加载图片集 -->
    <div class="image-section">
      <Set v-for="set in pictureSets" :key="set.id" :setData="set" @showDetails="handleShowDetails" />
      <!-- 侧边功能栏 -->
      <div class="picture-function-bar">
        <FunctionBar :buttons="functionButtons" />
      </div>
    </div>

    <!-- 显示详情的面板 -->
    <DisplayPanel v-if="currentSet" :set="currentSet" @close="handleClosePanel" @switchSet="handleSwitchSet" />

    <!-- Modal -->
    <Modal :visible="isModalVisible" @close="closeModal">
      <template v-if="modalType === 'uploadPicture'" #title>
        <div style="margin-bottom: 20px;">
          <div class="drag-drop-area" :style="{ backgroundImage: 'url(' + previewImage + ')' }"
            @click="triggerFileInput" @drop.prevent="handleDrop" @dragover.prevent>
            点击或拖拽上传图片
          </div>
          <input type="file" id="image-input" accept="image/*" @change="handleImageChange" style="display: none;" />
        </div>
      </template>
      <template v-if="modalType === 'uploadPicture'" #content>
        <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px;">
          <label for="image-name" class="label">图片名称：</label>
          <input v-model="imageName" type="text" id="image-name" class="input-field" placeholder="输入图片名称..."
            maxlength="15" />
        </div>
        <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px;">
          <label for="image-description" class="label">图片描述：</label>
          <textarea v-model="imageDescription" class="input-field" placeholder="输入图片描述..." maxlength="200"
            style="resize: none; height: 110px;"></textarea>
        </div>
      </template>
      <template v-if="modalType === 'uploadPicture'" #footer>
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
          <button class="confirmUploadImage" @click="confirmUploadImage">确认上传</button>
        </div>
      </template>
    </Modal>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import FunctionBar from '@/components/FunctionBar.vue';
import Set from '@/components/Set.vue';
import DisplayPanel from '@/components/DisplayPanel.vue';
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';

const { isModalVisible, modalType, openModal, closeModal } = useModal();

const imageName = ref(''); // 图片名称
const imageDescription = ref(''); // 图片描述
const selectedFile = ref(null); // 选中的图片文件
const previewImage = ref(null); // 预览图片的 URL
const pictureSets = ref([]); // 存储图片集数据
const currentSet = ref(null); // 当前展示的图片集
const currentIndex = ref(0); // 当前显示的 set 索引
const functionButtons = ref([
  {
    text: '上传',
    icon: '/icon/upload.svg',
    onClick: uploadPicture,
  },
]);

// 打开上传图片面板
function uploadPicture() {
  openModal('uploadPicture'); // 调用 useModal 中的 openModal
}

// 触发文件选择框
const triggerFileInput = () => {
  document.getElementById('image-input').click();
};

// 处理图片选择变化
const handleImageChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
    previewImage.value = URL.createObjectURL(file); // 预览图片
  }
};

// 处理拖拽上传
const handleDrop = (event) => {
  const file = event.dataTransfer.files[0];
  if (file) {
    selectedFile.value = file;
    previewImage.value = URL.createObjectURL(file); // 预览图片
  }
};

// 上传图片
const confirmUploadImage = async () => {
  if (!selectedFile.value || !imageName.value || !imageDescription.value) {
    alert("请填写所有必要信息并上传图片");
    return;
  }

  // 创建 FormData 对象，用于发送图片和表单信息
  const formData = new FormData();
  formData.append('image_input', selectedFile.value);
  formData.append('name', imageName.value);
  formData.append('description', imageDescription.value);

  try {
    // 发送 POST 请求上传图片
    const response = await axios.post('/api/upload_image', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    if (response.data.success) {
      alert('图片上传成功');
      // 清空表单和预览
      imageName.value = '';
      imageDescription.value = '';
      selectedFile.value = null;
      previewImage.value = null;
    }
  } catch (error) {
    console.error('图片上传失败:', error);
  }
};

// 页面加载时获取图片集数据
onMounted(async () => {
  try {
    // 请求图片集信息
    const response = await fetch('/api/get_sets');
    const imageSets = await response.json();

    // 检查是否有返回的图片集信息
    if (!Array.isArray(imageSets) || imageSets.length === 0) {
      console.log('No valid image sets found.');
      return; // 不进行任何渲染
    }

    // 遍历每个 set 并请求图片
    for (const imageSet of imageSets) {
      if (imageSet.image_url) {
        try {
          // 请求图片的 blob 数据
          const ImageUrl = `/api${imageSet.image_url}`;
          const imageResponse = await axios.get(ImageUrl, { responseType: 'blob' });

          // 将 blob 转换为可展示的图片 URL
          imageSet.imageBlobUrl = URL.createObjectURL(imageResponse.data);

        } catch (error) {
          console.error(`Failed to load image for set ${imageSet.id}:`, error);
        }
      }
    }

    pictureSets.value = imageSets; // 更新图片集数据
  } catch (error) {
    console.error('Error fetching sets:', error);
  }
});

// 处理显示详情的事件
const handleShowDetails = async (set) => {
  currentSet.value = set;
  currentIndex.value = pictureSets.value.findIndex((s) => s.id === set.id);

  // 获取当前图片集的评论
  currentSet.value.comments = await fetchComments(set.id);
};

// 关闭展示面板
const handleClosePanel = () => {
  currentSet.value = null;
};

// 左右切换图片集
const handleSwitchSet = async (direction) => {
  if (direction === 'left') {
    currentIndex.value = (currentIndex.value - 1 + pictureSets.value.length) % pictureSets.value.length;
  } else if (direction === 'right') {
    currentIndex.value = (currentIndex.value + 1) % pictureSets.value.length;
  }
  currentSet.value = pictureSets.value[currentIndex.value]; // 更新当前显示的图片集

  // 获取当前图片集的评论
  currentSet.value.comments = await fetchComments(currentSet.value.id);
};

// 获取当前图片集的评论
const fetchComments = async (imageId) => {
  try {
    const response = await fetch(`/api/get_comments?image_id=${imageId}`);
    const comments = await response.json();

    // 为每个评论的头像创建一个 Blob URL
    for (let comment of comments) {
      const avatarUrl = `/api${comment.avatar}`;
      const avatarResponse = await axios.get(avatarUrl, { responseType: 'blob' });
      comment.avatar = URL.createObjectURL(avatarResponse.data);  // 使用 Blob 创建头像的 URL
    }

    return comments;
  } catch (error) {
    console.error('Error fetching comments:', error);
    return [];
  }
};
</script>


<style scoped>
.fulilianpicture {
  padding-top: 60px;
}

/* 内容部分 */
.image-section {
  width: 100%;
  min-width: 1280px;
  position: relative;
  display: flex;
  padding: 20px 100px;
  /* 上下 左右 */
  gap: 30px;
  z-index: 1;
  flex-wrap: wrap;
  /* 允许换行 */
  overflow: hidden;
}

.picture-function-bar {
  position: fixed;
  width: 150px;
  right: 0;
  top: 50%;
  height: 50%;
  transform: translateY(-50%);
}

/* 拖拽上传 */
.drag-drop-area {
  position: relative;
  width: 500px;
  height: 350px;
  border: 2px dashed #ccc;
  background-color: #f8f8f8;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  font: 100 30px '程荣光刻楷';
  color: #7b7b7b;
  cursor: pointer;
}

.preview-image {
  position: absolute;
  width: 100%;
  height: 100%;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
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
  width: 300px;
  height: 35px;
  padding: 5px 10px;
}

/* 确认上传按钮 */
.confirmUploadImage {
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