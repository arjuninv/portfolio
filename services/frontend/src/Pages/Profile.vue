
<template>
    <div>
        <div class="hidden-md-and-up mt-0" style="overflow: auto; white-space: nowrap; margin-left: -13px; width: 100vw; box-shadow: -2px 7px 14px -10px rgba(0, 0, 0, 0.2)">
          <v-btn
            class="ma-0"
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
        <div class="hidden-sm-and-down" style="overflow: auto; white-space: nowrap;">
          <v-btn
            class="ma-0"
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