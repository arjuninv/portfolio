<template>
  <v-app>
    <div>
      <v-app-bar
        fixed
        color="white"
        elevate-on-scroll
      >
      <v-toolbar-title>{{apps[app].text}}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="black" tile text href="https://github.com/ArjunInventor/portfolio/" target="_blank">Source</v-btn>
    </v-app-bar>
    </div>
    <div style="height: 64px"></div>
    <v-container class="pt-0" style="max-width: 1280px;">
      <v-row class="d-flex align-content-start flex-wrap flex-column flex-md-row">
        <v-col
          class="ma-0 py-0"
          :cols="12"
          md="3"
        >
        <v-row>
          <v-col 
            :cols="5"
            :md="12"
            sm="3"  
          >
            <v-card
              outlined
              ripple
              >
              <v-img
                style="border-radius: 4px"
                :src="img_src"
                :lazy-src="lazy_img_src"
              ></v-img>
            </v-card>
          </v-col>
          <v-col 
            :cols="7"
            :md="12"
            sm="5"
          >
            <h2 class="headline mt-4">{{ name }}</h2> 
            <span class="text--secondary">{{ bio }}</span><br>
            <!-- <div class="mt-2">
              <v-chip
                class="mr-2 deep-purple--text"
                color="deep-purple accent-2"
                target="_blank" :href="'mailto:' + email"
                outlined
              >
                <v-icon left>mdi-email</v-icon>
                Email
              </v-chip>
            </div> -->
            <a target="_blank" :href="'mailto:' + email" style="text-decoration: none" class="deep-purple--text text--accent-4 caption">{{ email }}</a>
          </v-col>
        </v-row>

          <v-card
            v-if="!loading"
            class="mx-auto mt-4 hidden-sm-and-down"
            max-width="300"
            outlined
          >
            <v-list dense>
              <v-list-item-group v-model="app" color="deep-purple accent-4">
                <v-list-item
                  v-for="(app, i) in apps"
                  :key="i"
                >
                  <v-list-item-icon>
                    <v-icon v-text="app.icon"></v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title v-text="app.text"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>

        </v-col>
        <v-col
          :cols="12"
          md="9"  
        >
          <Profile v-if="apps[app].text == 'Profile' && pages" :pages="pages" />
          <Logs v-if="apps[app].text == 'Logs'" />
          <Blog v-if="apps[app].text == 'Blog'" />
  
        </v-col>
      </v-row>
      <div class="hidden-md-and-up" style="height: 56px"></div>
      <v-overlay :value="loading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    </v-container>
    <v-bottom-navigation
    class="hidden-md-and-up"
    v-model="app"
    color="deep-purple accent-4"
    horizontal
    style="position: fixed;
    bottom: 0px;"
  >
    <v-btn 
      v-for="(a, i) in apps"
      :key="i">
      <span>{{a['text']}}</span>
      <v-icon>{{a['icon']}}</v-icon>
    </v-btn>
  </v-bottom-navigation>
  </v-app>
</template>

<script>

import Profile from './Pages/Profile'
import Blog from './Pages/Blog'
import Logs from './Pages/Logs'

export default {
  name: 'App',

  components: {
    Profile,
    Logs,
    Blog
  },

  data: () => ({
    loading: true,
    img_src: "",
    lazy_img_src: "",
    name: "",
    bio: "",
    email: "",
    pages: [],
    app: 0,
    apps: [
      {
        icon: "mdi-account",
        text: "Profile",
        rel_path: "/profile"
      },
      {
        icon: "mdi-post-outline",
        text: "Blog",
        rel_path: "/blog"
      },
      {
        icon: "mdi-format-list-bulleted-triangle",
        text: "Logs",
        rel_path: "/logs"
      },
    ]
  }),
  mounted() {
    fetch(`${this.$host}/api/profile`)
    .then(response => response.json())
    .then(j => {
      this.loading = false
      this.name = j.data.name
        this.bio = j.data.bio
        this.img_src = j.data.img_src
        this.lazy_img_src = j.data.lazy_img_src
        this.email = j.data.email
        this.pages = j.data.pages
    });
    this.apps.forEach((element, index) => {
        if(element.rel_path == '/' + this.$route.name) {
          this.app = index
        }
    });
  },
  methods: {
    app_change(index) {
      this.$router.push({path: this.apps[index].rel_path + "/"})
    }
  },
  watch: {
    '$route' (to) {
        document.title = to.meta.title || 'Arjun S'
    },
    app: function(val) {
        this.app_change(val);
    }
  }
};
</script>

<style>
  html { overflow-y: auto }
</style>