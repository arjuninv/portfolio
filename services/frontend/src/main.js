import Vue from 'vue'

import Main from './Main.vue'
import vuetify from './plugins/vuetify';
import { router } from './_helpers';

Vue.config.productionTip = false

Vue.prototype.$host = '';
if (process.env.NODE_ENV === 'development') {
  console.log('In development mode');
  Vue.prototype.$host = 'https://arjuninventor.com';
}


new Vue({
  vuetify,
  router,
  render: h => h(Main)
}).$mount('#app')
