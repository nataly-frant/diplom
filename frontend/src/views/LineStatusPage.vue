<template>
  <div>
    <h1 class="ml-4">Статусы производственных линий</h1>
    <StatusTable :data="lineItems" :statusMap="statusMap"/>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import api from '@/api'
import StatusTable from '@/components/StatusTable.vue'

const lineStatus = ref(null)
const lineItems = ref({})

const statusMap = {
  active: {color: 'green', icon: 'mdi-check-circle'},
  idle: {color: 'grey', icon: 'mdi-clock-outline'},
  error: {color: 'red', icon: 'mdi-alert-circle'}
}

onMounted(async () => {
  const response = await api.get('/line_status/')
  lineStatus.value = response.data
  if (lineStatus.value.data_json) {
    lineItems.value = lineStatus.value.data_json
  }
})
</script>
