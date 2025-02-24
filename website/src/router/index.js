import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('../views/index.vue')
  },
  {
    path: '/ide',
    name: 'IDE',
    component: () => import('../views/ide/codeIde.vue')
  },
  {
    path: '/algorithm',
    name: 'Algorithm',
    component: () => import('../views/algorithm/algorithmIndex.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
