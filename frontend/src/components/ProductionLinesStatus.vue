<template>
  <div class="production-lines-status">
    <v-list dense>
      <v-list-item v-for="(line, index) in lines" :key="index">
        <v-list-item-content>
          <v-list-item-title>
            {{ line.name }} — {{ line.product }}
          </v-list-item-title>
          <v-list-item-subtitle>
            Статус: <v-chip :color="statusColor(line.status)" dark>{{ line.status }}</v-chip> | Выполнение: {{ line.progress }}%
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script setup>
const lines = [
  { name: 'Линия 1', product: 'Черный чай', status: 'В работе', progress: 67 },
  { name: 'Линия 2', product: 'Зеленый чай', status: 'Остановлена', progress: 20 }
]

function statusColor(status) {
  switch (status) {
    case 'В работе':
      return 'blue'
    case 'Остановлена':
      return 'red'
    case 'Завершена':
      return 'green'
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
