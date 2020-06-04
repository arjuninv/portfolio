import Vue from 'vue';
import Router from 'vue-router';

import App from '../App.vue'
import Admin from '../Admin.vue'


Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/profile', name: 'profile', component: App, meta: {title: 'Arjun S - Profile'}},
    { path: '/profile/:page', name: 'profile', component: App, meta: {title: 'Arjun S - Profile'}},
    { path: '/logs', name: 'logs', component: App, meta: {title: 'Arjun S - Logs'}},
    { path: '/logs/:log', name: 'logs', component: App, meta: {title: 'Arjun S - Logs'}},
    { path: '/blog', name: 'blog', component: App, meta: {title: 'Arjun S - Blog'}},
    { path: '/admin', name: 'admin', component: Admin, meta: {title: 'Arjun S - Admin'}},
    { path: '/*', redirect: '/profile/' }
  ]
});