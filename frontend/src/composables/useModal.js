import { ref } from 'vue';

export function useModal() {
  const isModalVisible = ref(false);
  const modalType = ref('');

  function openModal(type) {
    modalType.value = type; // 设置 modal 类型
    isModalVisible.value = true; // 打开 modal
  }

  function closeModal() {
    isModalVisible.value = false; // 关闭 modal
  }

  return { isModalVisible, modalType, openModal, closeModal };
}