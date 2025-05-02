<template>
  <div class="important-notifications">
    <v-alert
      v-for="(note, index) in notifications"
      :key="index"
      type="warning"
      dense
      outlined
      class="mb-1 pa-1"
    >
      {{ note }}
    </v-alert>
  </div>
</template>

<script setup>
const notifications = [
  'Необходима проверка линии №3',
  'Поступило новое сырье для Зеленого чая'
]
</script>

<style scoped>
.important-notifications {
  margin-top: 1rem;
}
</style>
