<template>
    <div>
        <v-select
          :logs="logs"
          label="Select log"
          outlined
        ></v-select>
        <v-row no-gutters style="flex-wrap: nowrap;">
            <v-col
                class="flex-grow-1 flex-shrink-0"
            >
            <p>Description</p>
            </v-col>

            <v-col
                class="flex-grow-0 flex-shrink-0"
            >
            <v-btn depressed large color="primary">Subscribe</v-btn>
            </v-col>
        </v-row>

    </div>
</template>
