<template>
  <div v-if="visible" class="modal-mask">
    <div class="modal-container">
      <!-- 关闭按钮 -->
      <span class="modalClose" @click="$emit('close')">&times;</span>

      <slot name="title"></slot>

      <slot name="subtitle"></slot>

      <slot name="content"></slot> <!-- 动态内容区域 -->

      <slot name="footer"></slot> <!-- 可选的底部内容 -->
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
})
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-container {
  position: relative;
  background: white;
  padding: 30px 50px;
  border-radius: 8px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
  max-width: 1100px;
  max-height: 700px;
  width: fit-content;
  height: fit-content;
  overflow-y: auto;
}
.modalClose {
  position: absolute;
  top: 2%;
  right: 2%;
  font-size: 34px;
  cursor: pointer;
}
</style>
