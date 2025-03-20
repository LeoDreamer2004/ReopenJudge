<template>
  <div class="header">
    <span class="link" v-for="(dir, index) in display.split('/')" :key="index">
      <a :href="getlink(index)" class="pr-2">{{ dir }}</a>
      <span v-if="index < display.split('/').length - 1" class="pr-2">></span>
    </span>
    <h2 v-text="getTitle()"></h2>
  </div>
</template>

<script>
export default {
  props: {
    link: {
      type: String,
      default: "/"
    },
    display: {
      type: String,
      default: "首页"
    }
  },
  methods: {
    getlink(index) {
      if (index === 0) {
        return '/'
      }
      return this.link.split('/').slice(0, index + 1).join('/')
    },
    getTitle() {
      return this.display.split('/').slice(-1)[0]
    }
  },
}

</script>

<style>
.header {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  /* height: 180px; */
  margin-bottom: 40px;
  background-color: #333;
  color: white;
  padding: 20px 150px 20px 150px;
  min-width: 1000px;
}

.header .user-details {
  background-color: rgba(200, 210, 210, 0.8);
  height: 60px;
  border-radius: 10px;
  padding: 40px 20px 25px;
  position: absolute;
  right: 50px;
  top: -10px;
  float: right;
  display: flex;
  justify-content: space-between;
  vertical-align: middle;
  align-items: center;
}

.user-details .user-item {
  color: rgba(26, 28, 29, 0.9);
  margin-left: 5px;
  margin-right: 5px;
}

.header h2 {
  margin-top: 10px;
  padding-bottom: 10px;
  font-weight: bolder;
}

.header .link * {
  font-size: 15px;
  color: lightgray;
}
</style>
