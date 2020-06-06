<template>
    <div>
        <div class="hidden-md-and-up mt-0" style="height: 10px; overflow: auto; white-space: nowrap; margin-left: -13px; width: 100vw; box-shadow: -2px 7px 14px -10px rgba(0, 0, 0, 0.2)">
        </div>
        <v-progress-linear
            indeterminate
            color="deep-purple accent-4"
            v-if="loading"
        ></v-progress-linear>
        <v-card
            outlined
            class="post mb-5"
            v-for="post in posts"
            :key="post.title"
            >
                <h3 class="title mb-3">{{post.title}}</h3>
                <div v-html="post.content"></div>
        </v-card>
    </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
      posts: [],
      loading: true
  }),
  mounted() {
      fetch('https://api.allorigins.win/get?url=https://medium.com/feed/@Arjuninventor')
        .then(response => response.json())
        .then(str => (new window.DOMParser()).parseFromString(str.contents, "text/xml"))
        .then(data => {
            this.posts = []
            var posts_obj = data.getElementsByTagName('channel')[0].children;
            posts_obj.forEach(element => {
                if (element.nodeName == 'item')
                    {   
                        var post = {};
                        element.children.forEach(e => {
                            if (e.nodeName == 'title')
                                post['title'] = e.textContent
                            if (e.nodeName == 'content:encoded')
                                post['content'] = e.textContent
                        });
                        if (post['content'].startsWith("<h3>" + post['title'] + "</h3>"))
                            post['content'] = post['content'].replace("<h3>" + post['title'] + "</h3>", "")  
                        this.posts.push(post)
                    }
            });
            this.loading = false;
        })
  }
}
</script>

<style scoped>
.post >>> img {
    width: 100%
}
.post {
    padding: 24px
}
</style>