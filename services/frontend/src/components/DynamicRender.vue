<template>
    <div>
        <v-progress-linear
            indeterminate
            color="deep-purple accent-4"
            v-if="loading"
        ></v-progress-linear>
        <div v-for="content in contents" :key="content.id">
            <!-- Paragraph -->
            <div>
                <h3 class="mt-4 title">{{content.title}}</h3>
                <v-card class="pa-4 mt-2 mb-8" outlined>
                    <!-- Paragraph -->
                    <p v-if="content.type=='p'" v-html="content.data.text"></p>

                    <!-- List -->
                    <div  v-if="content.type=='list'" >
                    <div
                        v-for="(item, index) in content.data.items"
                        :key="index"
                    >
                        <h4 class="subtitle">{{item.title}}</h4>
                            <p>{{item.subtitle}}</p>
                            <v-list-item-subtitle>{{item.description}}</v-list-item-subtitle>
                    </div>
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
            fetch(`https://arjuninventor.com/api/profile/page${rel_path}`)
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