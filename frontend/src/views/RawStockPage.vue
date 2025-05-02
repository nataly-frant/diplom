<template>
  <div>
    <h1 class="ml-4">Статусы склада сырья</h1>
    <StatusTable :data="stockItems" :statusMap="statusMap" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import StatusTable from '@/components/StatusTable.vue'

const stockItems = ref({})

const statusMap = {
  available: { color: 'green', icon: 'mdi-check-circle' },
  low: { color: 'orange', icon: 'mdi-alert' },
  empty: { color: 'red', icon: 'mdi-close-circle' }
}

onMounted(async () => {
  const response = await api.get('/raw_stock/')
  const stockData = response.data

  if (stockData.data_json) {
    stockItems.value = stockData.data_json
  } else {
    stockItems.value = {}
  }
})
</script>
