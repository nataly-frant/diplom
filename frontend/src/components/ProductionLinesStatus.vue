<template>
  <div class="production-lines-status">
    <v-list dense>
      <v-list-item v-for="(line, index) in lines" :key="index">
        <v-list-item-content>
          <v-list-item-title>
            <div class="d-flex justify-space-between align-center">
              <span>{{ line.name }} — {{ line.product }}</span>
              <span><v-chip :color="statusColor(line.status)" dark>{{ line.status }}</v-chip></span>
            </div>
          </v-list-item-title>
          <v-list-item-subtitle>
            Выполнение плана: {{ line.progress }}%
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script setup>
const lines = [
  {name: 'Линия 1', product: 'Черный чай', status: 'В работе', progress: 70},
  {name: 'Линия 2', product: 'Зеленый чай', status: 'Остановлена', progress: 49},
  {name: 'Линия 3', product: 'Травяной чай', status: 'В работе', progress: 90}
]

function statusColor(status) {
  switch (status) {
    case 'В работе':
      return 'green'
    case 'Остановлена':
      return 'red'
    case 'Завершена':
      return 'blue'
    default:
      return 'grey'
  }
}
</script>

<style scoped>
.production-lines-status {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
</style>
