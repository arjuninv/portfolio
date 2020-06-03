
<template>
    <div>
        <div style="overflow: auto; white-space: nowrap;">
            <v-btn
              class="ma-1"
              v-bind:class="{'v-btn--active': (current_page == index)}"
              color="deep-purple accent-4"
              :v-model="current_page"
              v-for="(page, index) in pages"
              :key="page.index"
              @click="profile_page_change(index)"
              tile text large 
            >
              {{page.title}}
            </v-btn>
          </div>
        <DynamicRender v-if="pages[current_page]" class="pa-2" :page="pages[current_page]" />
    </div>
</template>

<script>
import DynamicRender from '../components/DynamicRender'

export default {
  name: 'Profile',
  props: ['pages'],
  data : () => ({
    current_page: 0,
    page_map: {}
  }),
  components: {
      DynamicRender
  },
  watch: {
      pages: {
          immediate: true, 
          handler(val) {
              if(!this.$route.params.page) {
                this.current_page = 0
              } else {
                if(val){
                  val.forEach((element, index) => {
                    if(element.rel_path == '/' + this.$route.params.page) {
                      this.current_page = index
                    }
                  });
                }
              }
          }
      }
  },
  methods: {
      profile_page_change(index) {
        this.current_page = index
        this.$router.push({ path: '/profile' + this.pages[this.current_page].rel_path})
      },
  }
}
</script>