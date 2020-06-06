<template>
    <div>
        <v-select
          :items="logs"
          v-model="selected_log"
          item-text="name"
          label="Select log"
          color="deep-purple accent-4"
          :loading="loading"
          outlined
        ></v-select>
        <div v-if="data != null">
            <v-card outlined
                class="pa-4 pb-1 mb-2"
                v-for="item in data"
                :key="item.timestamp">
                    <p>{{item.data}}</p>
                    <p width="100%" class="overline text-right">{{item.timestamp}}</p>
            </v-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Logs',
    data: () => ({
        logs: [],
        data: null,
        selected_log: null,
        loading: true
    }),
    mounted() {
        fetch(`${this.$host}/api/logs`)
        .then(response => response.json())
        .then(j => {
            this.loading = false
            this.logs = j.logs
            if(this.$route.params.log) {
                this.selected_log = this.$route.params.log
            } else {
                this.selected_log = this.logs[0]
            }
        });
    },
    watch: {
        selected_log: {
            immediate: false, 
            handler(val) {
                        console.log("asd")

                if (val && val != this.$route.params.log) {
                    this.$router.push({ path: '/logs/' + val})
                } else if (val) {
                     fetch(`/api/logs/log/${val}`)
                    .then(response => response.json())
                    .then(j => {
                        console.log(j.logs)
                        this.data = j.logs
                    });
                }
            }
        }
    }
}
</script>
