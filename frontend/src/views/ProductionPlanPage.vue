<template>
  <div>
    <h1 class="ml-4">Производственный план</h1>
    <StatusTable :data="planItems" :statusMap="statusMap"/>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import api from '@/api'
import StatusTable from '@/components/StatusTable.vue'

const planItems = ref({})

const statusMap = {
  scheduled: {color: 'blue', icon: 'mdi-calendar'},
  in_progress: {color: 'orange', icon: 'mdi-progress-clock'},
  completed: {color: 'green', icon: 'mdi-check-circle'},
  delayed: {color: 'red', icon: 'mdi-alert-circle'}
}

onMounted(async () => {
  const response = await api.get('/production_plan/')
  const planData = response.data

  if (planData.data_json) {
    planItems.value = planData.data_json
  } else {
    planItems.value = {}
  }
})
</script>
