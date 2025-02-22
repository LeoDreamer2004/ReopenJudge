<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="(problem, index) in problems" :key="index" style="display:block">
        {{ index }}-{{ problem.title }}-{{ problem.description }}-{{ problem.difficulty }}
      </li>
    </ul>
    <form action="">
      输入标题：<input type="text" placeholder="problem title" v-model="inputProblem.title"><br>
      输入描述：<input type="text" placeholder="problem description" v-model="inputProblem.description"><br>
      输入难度：<input type="number" placeholder="problem difficulty" v-model="inputProblem.difficulty"><br>
    </form>
    <button type="submit" @click="problemSubmit()">submit</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      inputProblem: {
        title: "",
        description: "",
        difficulty: 0,
      },
      problems: []
    }
  },
  methods: {
    loadProblems() {
      axios.get('http://127.0.0.1:8000/api/problems').then(res => {
        console.log(res.data)
        this.problems = res.data
      })
    },
    problemSubmit() {
      axios.post(`http://127.0.0.1:8000/api/problems/`, {
        title: this.inputProblem.title,
        description: this.inputProblem.description,
        difficulty: this.inputProblem.difficulty
      })
    }
  },
  created: function () {
    this.loadProblems()
  }
}
</script>
