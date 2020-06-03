import Vue from 'vue';
import Router from 'vue-router';

import App from '../App.vue'
import Admin from '../Admin.vue'


Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/profile/', name: 'profile', component: App},
    { path: '/profile/:page', name: 'profile', component: App},
    { path: '/logs', name: 'logs', component: App },
    { path: '/blog', name: 'blog', component: App },
    { path: '/admin', name: 'admin', component: Admin },
    { path: '/*', redirect: '/profile/' }
  ]
});