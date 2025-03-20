<script setup>
import Header from "@/components/pageHeader.vue";
import CodeEdit from "@/components/codeEdit.vue";
</script>

<template>
  <Header :link="'/ide'" :display="'首页/在线 IDE'"> </Header>
  <main class="container">
    <CodeEdit />
    <div class="ide-wrapper">
      <div class="io-container">
        <div class="input-container">
          <div class="io-title" for="input">
            <span class="pr-2">输入</span>
            <button class="btn btn-primary mr-2" id="submit" type="button">
              <span class="iconfont icon-bofang pr-2"></span>运行
            </button>
          </div>
          <textarea class="io form-control" id="input" name="input"></textarea>
        </div>
        <div class="output-container">
          <div class="io-title">
            <span class="pr-2">输出</span>
            <span id="usage">956ms/475KB</span>
          </div>
          <div class="io form-control" id="output"></div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url('https://at.alicdn.com/t/c/font_4837111_ocqofi9lmjs.css');

.io-container {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.io {
  resize: none;
  overflow-y: auto;
  width: 100%;
  height: 200px !important;
  font-family: Consolas, monospace;
  font-size: 18px;
}

.io-title {
  height: 40px;
  margin: 10px;
  font-size: 20px;
  align-items: center;
  justify-items: center;
  display: flex;
}

.input-container,
.output-container {
  width: 90%;
  height: 100%;
}
</style>
