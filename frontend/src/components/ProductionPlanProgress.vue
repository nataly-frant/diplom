<template>
  <div class="production-plan-progress">
    <v-row justify="center">
      <v-col v-for="(item, index) in plans" :key="index" cols="12" md="3">
        <div class="circle-container">
          <v-progress-circular
            :model-value="item.progress"
            :rotate="360"
            :size="100"
            :width="15"
            :color="progressColor(item.progress)"
          >
            <template v-slot:default> {{ item.progress }} %</template>
          </v-progress-circular>
          <div class="product-name">{{ item.product }}</div>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
const plans = [
  {product: 'Черный чай', progress: 70},
  {product: 'Зеленый чай', progress: 49},
  {product: 'Травяной сбор', progress: 90}
]

function progressColor(value) {
  if (value >= 80) return 'green'
  if (value >= 50) return 'blue'
  return 'red'
}
</script>

<style scoped>
.production-plan-progress {
  text-align: center;
}

.circle-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1rem;
}

.product-name {
  margin-top: 0.5rem;
  font-size: 14px;
  color: #555;
  text-align: center;
}
</style>
