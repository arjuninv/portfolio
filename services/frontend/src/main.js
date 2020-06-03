import Vue from 'vue'

import Main from './Main.vue'
import vuetify from './plugins/vuetify';
import { router } from './_helpers';

Vue.prototype.PROFILE_API_VERSION = 'v1';

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(Main)
}).$mount('#app')
