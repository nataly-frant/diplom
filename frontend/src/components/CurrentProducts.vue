<template>
  <div class="current-products">
    <v-list dense>
      <v-list-item v-for="(product, index) in products" :key="index">
        <v-list-item-content>
          <v-list-item-title>{{ product.name }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script setup>
const products = [
  { name: 'Черный чай' },
  { name: 'Зеленый чай' },
  { name: 'Травяной сбор' }
]
</script>

<style scoped>
.current-products {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
