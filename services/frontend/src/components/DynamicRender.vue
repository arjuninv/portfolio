<template>
    <div class="pt-0">
        <v-progress-linear
            class="hidden-md-and-up"        
            indeterminate
            color="deep-purple accent-4 mt-0"
            style="margin-left: -20px; width: 100vw;"
            v-if="loading"
        ></v-progress-linear>
        <v-progress-linear
            class="hidden-sm-and-down"
            indeterminate
            color="deep-purple accent-4 mt-0"
            style="margin-left: -8px;"
            v-if="loading"
        ></v-progress-linear>
        
        <div v-for="content in contents" :key="content.id">
            <!-- Paragraph -->
            <div>
                <h3 class="mt-4 title">{{content.title}}</h3>
                <v-card class="pa-4 mt-2 mb-8" outlined>
                    <!-- Paragraph -->
                    <p v-if="content.type=='p'" class="body-2 text--secondary" v-html="content.data.text"></p>

                    <!-- List -->
                    <div  v-if="content.type=='list'" >
                            <v-list-item three-line 
                                v-for="(item, index) in content.data.items"
                                :key="index"
                                :href="item.action"
                                target="_blank"
                            >
                                <v-list-item-content>
                                <h4 class="subtitle">{{item.title}}</h4>
                                    <p class="subtitle-1 my-0">{{item.subtitle}}</p>
                                    <p class="body-2 text--secondary mb-0" v-html="item.description.replace(/\n/g, '<br>')"></p>
                                </v-list-item-content>
                                <v-img
                                    tile
                                    class="mb-auto ma-3"
                                    :max-width="80"
                                    :height="80"
                                    :src="item.image"
                                ></v-img>
                            </v-list-item>
                </div>
                </v-card>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DynamicRender',
    loading: true,
    props: ['page'],
    data: () => ({
        contents: [],
    }),
    methods: {
        update_page(rel_path) {
         this.loading = true;
            fetch(`${this.$host}/api/profile/page${rel_path}`)
            .then(response => response.json())
            .then(j => {
                this.contents = j.content;
                this.loading = false;
            });                
        }
    },
    watch: {
        page: {
            immediate: true, 
            handler(val) {
                this.contents = []
                this.update_page((val.rel_path == '/' ? '/root' : val.rel_path))
            }
        }
    },
}
</script>