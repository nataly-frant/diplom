<template>
  <div>
    <h1 class="ml-4">Склад готовой продукции</h1>
    <StatusTable :data="finishStockItems" :statusMap="statusMap"/>
  </div>
</template>
<script setup>

import {ref, onMounted} from 'vue'
import api from '@/api'
import StatusTable from '@/components/StatusTable.vue'

const finishStockItems = ref({})

const statusMap = {
  full: {color: 'green', icon: 'mdi-check-circle'},
  low: {color: 'orange', icon: 'mdi-alert'},
  empty: {color: 'red', icon: 'mdi-close-circle'}
}

onMounted(async () => {
  const response = await api.get('/finished_stock/')
  const finishStockData = response.data

  if (finishStockData.data_json) {
    finishStockItems.value = finishStockData.data_json
  } else {
    finishStockItems.value = {}
  }
})
</script>
