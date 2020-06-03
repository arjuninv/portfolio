<template>
    <div>
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
    props: ['page'],
    data: () => ({
        contents: [],
    }),
    methods: {
        update_page(rel_path) {
         // fetch(`/api/${this.PROFILE_API_VERSION}/profile/page/`)
            fetch(`/api/${this.PROFILE_API_VERSION}/profile/page${rel_path}`)
            .then(response => response.json())
            .then(j => {
                this.contents = j.content
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