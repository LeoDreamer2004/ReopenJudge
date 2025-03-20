<template>
  <div>
    <div class="form-inline">
      <span class="form-inline-item">选择编译器</span>
      <div class="form-inline-item">
        <select class="form-control form-control-placeholder mb-3 ml-3 mt-3" v-model="lang">
          <option value="Python">Python (python 3.13.2)</option>
          <option value="C++">C++ (g++ 14.2.1)</option>
        </select>
      </div>
    </div>

    <Codemirror v-if="lang === 'Python'" v-model:value="code" :options="py_opt" ref="editor" border height="300"
      width="100%" @ready="onReady" />

    <Codemirror v-if="lang === 'C++'" v-model:value="code" :options="c_opt" ref="editor2" border height="300"
      width="100%" @ready="onReady" />
  </div>
</template>

<script>
import { ref } from 'vue';
import Codemirror from 'codemirror-editor-vue3';
import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/idea.css';
import 'codemirror/mode/python/python.js';
import 'codemirror/mode/clike/clike.js';
import 'codemirror/addon/hint/show-hint.css';
import 'codemirror/addon/hint/show-hint';

export default {
  components: { Codemirror },
  setup() {
    const code = ref("");
    const lang = ref("Python");

    const py_opt = {
      mode: 'text/x-python',
      theme: 'default',
      line: true,
      lineNumbers: true,
      lineWrapping: true,
      tabSize: 4,
      hintOptions: {
        completeSingle: false,
      },
    };

    const c_opt = {
      mode: 'text/x-c++src',
      theme: 'default',
      line: true,
      lineNumbers: true,
      lineWrapping: true,
      tabSize: 4,
      hintOptions: {
        completeSingle: false,
      },
    };

    const onReady = (cmEditor) => {
      cmEditor.on('inputRead', function (cm, location) {
        if (/[a-zA-Z]/.test(location.text[0])) {
          cm.showHint();
        }
      });
    };

    return {
      code,
      py_opt,
      c_opt,
      lang,
      onReady,
    };
  },
};
</script>

<style>
.CodeMirror-code {
  font-size: large !important;
}
</style>
