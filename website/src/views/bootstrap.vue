<script setup>
import NavBar from '@/components/navBar.vue';
</script>

<template>
  <NavBar />
  <div>
    <!-- 使用 Bootstrap 样式的按钮 -->
    <button class="btn btn-primary" @click="handleClick">
      {{ buttonText }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'BootstrapButton',
  props: {
    buttonText: {
      type: String,
      default: 'Click Me' // 默认按钮文本
    }
  },
  methods: {
    handleClick() {
      // 点击按钮时触发的事件
      this.$emit('button-clicked');
    }
  }
};
</script>

<style scoped>
/* 如果需要自定义样式，可以在这里添加 */
</style>
