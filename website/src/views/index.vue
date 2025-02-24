<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import Foot from "@/components/indexFooter.vue";
</script>

<template>
  <div>
    <main class="container pt-4" role="main">
      <div class="jumbotron mb-1" id="welcome">
        <h1 class="display-4">ReopenJudge</h1>
        <p class="lead">
          --OpenJudge new ver-- <br />
          享受设计算法的过程，提升您的编程能力。 <br />
        </p>
        <div>
          <span class="blinking-code" style="float: right;"></span>
        </div>
      </div>
      <div id="start-arrow-container">
        <div id="start-arrow">
          <a class="iconfont icon-icon_xiangxia_ no-dec" href="/problems"></a>
        </div>
      </div>
    </main>
    <Foot />
  </div>
</template>

<style lang="css" scoped>
@import url('https://at.alicdn.com/t/c/font_4837111_okbzyuc0h2.css');

#welcome {
  animation: flowUp 0.5s ease-in-out 1 !important;
  background-color: rgba(230, 230, 230, 0.5) !important;
  border-radius: 15px;
  padding: 60px 40px;
}

@keyframes flowUp {
  0% {
    transform: translateY(10px);
    opacity: 0.3;
  }

  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes floatUpDown {
  0% {
    transform: translateY(0);
    opacity: 0.5;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }

  60% {
    transform: translateY(5px);
    opacity: 1;
  }

  100% {
    transform: translateY(0);
    opacity: 0.5;
  }
}
</style>
