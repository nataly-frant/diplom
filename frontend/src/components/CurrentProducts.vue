<template>
  <div class="current-products">
    <v-list dense>
      <v-list-item v-for="(product, index) in products" :key="index">
        <v-list-item-content>
          <v-list-item-title>{{ product.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ product.code }} &bull; {{ product.weight }} &bull; {{ product.serial }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script setup>
const products = [
  {name: 'Черный чай', code: 'BT-1449', weight: '500г', serial: 'A14491'},
  {name: 'Зеленый чай', code: 'GT-7845', weight: '250г', serial: 'Р78452'},
  {name: 'Травяной сбор', code: 'HT-158', weight: '100г', serial: 'Р1583'}
]
</script>

<style scoped>
.current-products {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
