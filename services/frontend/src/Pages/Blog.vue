<template>
    <div>
        Blog

        <v-card
            outlined
            class="post mt-5"
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
      posts: []
  }),
  mounted() {
      fetch('https://thingproxy.freeboard.io/fetch/https://medium.com/feed/@Arjuninventor')
        .then(response => response.text())
        .then(str => (new window.DOMParser()).parseFromString(str, "text/xml"))
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