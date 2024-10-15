<template>
  <div>
    <!-- 隐藏的文件上传 input -->
    <input ref="fileInput" type="file" accept="image/*" @change="onFileSelected" class="hidden" />

    <!-- 裁剪模态框 -->
    <Modal :visible="isModalVisible" @close="closeModal">
      <template v-if="modalType === 'imageCropper'" #title>
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
          <h2 style="font: 100 36px '程荣光刻楷';">上传头像</h2>
        </div>
      </template>
      <template v-if="modalType === 'imageCropper'" #subtitle>
        <div style="display: flex; justify-content: center; align-items: center;">
          <div class="cropper-container">
            <img ref="imagePreview" alt="裁剪预览" />
          </div>
        </div>
      </template>
      <template v-if="modalType === 'imageCropper'" #footer>
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
          <button id="confirmCrop" @click="confirmCrop">确认裁剪</button>
        </div>
      </template>
    </Modal>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';
import Cropper from 'cropperjs';
import 'cropperjs/dist/cropper.css';
import Modal from '@/components/Modal.vue';
import { useModal } from '@/composables/useModal';

const fileInput = ref(null);
const imagePreview = ref(null);
const cropper = ref(null);
const { isModalVisible, modalType, openModal, closeModal } = useModal();

// 触发文件上传
const triggerUpload = () => {
  fileInput.value.click();
};

// 使用 defineEmits 代替 emit
const emit = defineEmits(['upload']);

// 文件选择事件
const onFileSelected = async (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = async (e) => {
      // 设置图像数据后再打开模态框
      openModal('imageCropper'); // 先打开模态框

      // 使用 nextTick 确保模态框中的 img 元素已经挂载
      await nextTick();

      if (imagePreview.value) {
        imagePreview.value.src = e.target.result; // 设置图像的 src

        // 初始化 Cropper
        if (cropper.value) {
          cropper.value.destroy(); // 销毁之前的 Cropper 实例
        }
        cropper.value = new Cropper(imagePreview.value, {
          aspectRatio: 1,
          viewMode: 1,
        });
      } else {
        console.error("imagePreview is null");
      }
    };
    reader.readAsDataURL(file);
  }
};


// 确认裁剪
const confirmCrop = () => {
  const canvas = cropper.value.getCroppedCanvas({
    width: 1024,
    height: 1024,
  });
  canvas.toBlob((blob) => {
    emit('upload', blob); // 发射 upload 事件并传递裁剪后的图片
  });
  closeModal('imageCropper');
};


// 使用 defineExpose 将 triggerUpload 暴露给父组件
defineExpose({ triggerUpload });
</script>

<style scoped>
.hidden {
  display: none;
}

.cropper-container {
  width: 500px;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 裁剪面板图像预览 */
#imagePreview {
  width: 100%;
  height: 100%;
  /* 保持纵横比 */
  object-fit: cover;
}

/* 确认裁剪按钮 */
#confirmCrop {
    border-radius: 50px;
    padding: 12px 22px;
    font: 100 22px '程荣光刻楷';
    border: none;
    cursor: pointer;
    white-space: nowrap;
    background-color: #1551b1;
    color: #ffffff;
}
</style>
