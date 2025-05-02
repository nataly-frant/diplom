<template>
  <div>
    <v-card class="ma-4 pa-4" v-if="Object.keys(data).length > 0">
      <v-table>
        <thead>
        <tr>
          <th>Название</th>
          <th>Статус</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(status, name) in data" :key="name">
          <td>{{ name }}</td>
          <td>
            <v-chip
              :color="statusMap[status]?.color || 'grey'"
              dark
              class="ma-2"
            >
              <v-icon v-if="statusMap[status]?.icon" start>
                {{ statusMap[status].icon }}
              </v-icon>
              {{ status }}
            </v-chip>
          </td>
        </tr>
        </tbody>
      </v-table>
    </v-card>

    <v-alert
      v-else
      type="info"
      class="ma-4"
    >
      Нет данных для отображения.
    </v-alert>
  </div>
</template>

<script setup>
defineProps({
  data: {
    type: Object,
    required: true
  },
  statusMap: {
    type: Object,
    required: true
  }
})
</script>
