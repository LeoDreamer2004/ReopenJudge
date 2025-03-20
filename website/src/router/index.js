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
    component: () => import('../views/ide/onlineIde.vue')
  },
  {
    path: '/algorithm',
    name: 'Algorithm',
    component: () => import('../views/algorithm/algorithmIndex.vue')
  },

  // 嵌套 problem router
  {
    path: '/problems',
    name: 'Problems',
    children: [
      {
        path: '',
        name: 'ProblemList',
        component: () => import('../views/problem/problemList.vue')
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
