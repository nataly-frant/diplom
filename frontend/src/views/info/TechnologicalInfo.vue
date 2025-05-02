<template>
  <div>
    <h1 class="ml-4">Технологические карты</h1>
    <v-row>
      <v-col
        v-for="(line, index) in lines"
        :key="index"
        cols="12"
        md="6"
        lg="4"
      >
        <v-card class="pa-3">
          <v-card-title>{{ line.name }}</v-card-title>
          <v-card-text>
            {{ line.description }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import api from '@/api'

const lines = ref([])

onMounted(async () => {
  const response = await api.get('/info/technological-cards/')
  lines.value = response.data
})
</script>
