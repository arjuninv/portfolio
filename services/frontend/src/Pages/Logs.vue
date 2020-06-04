<template>
    <div>
        <v-select
          :items="logs"
          v-model="selected_log"
          item-text="name"
          label="Select log"
          color="deep-purple accent-4"
          outlined
        ></v-select>
        <v-row no-gutters style="flex-wrap: nowrap;">
            <v-col
                class="flex-grow-1 flex-shrink-0"
            >
            <p>{{logs_map[selected_log].description}}</p>
            </v-col>

            <v-col
                class="flex-grow-0 flex-shrink-0"
            >
            <v-btn outlined color="deep-purple accent-4">Subscribe</v-btn>
            </v-col>
        </v-row>
    </div>
</template>

<script>
export default {
    name: 'Logs',
    data: () => ({
        logs: [],
        logs_map: {},
        selected_log: null
    }),
    mounted() {
        fetch(`http://localhost:8082`)
        // fetch(`http://localhost:8081/`)
        .then(response => response.json())
        .then(j => {
            this.logs = j.data.logs
            this.selected_log = this.logs[0].name
            this.logs.forEach((element, index) => {
                this.logs_map[element.name] = {  index: index,
                                            rel_path: element.rel_path,
                                            description: element.description
                                        }
            });
        });
        

    },
}
</script>
