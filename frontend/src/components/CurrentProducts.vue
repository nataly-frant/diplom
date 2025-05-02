<template>
  <div class="current-products">
    <v-list dense>
      <v-list-item v-for="(product, index) in products" :key="index">
        <v-row no-gutters class="w-100 align-start">
          <v-col cols="10">
            <v-list-item-content>
              <v-list-item-title>{{ product.name }}</v-list-item-title>
              <v-list-item-subtitle>{{ product.code }} &bull; {{ product.weight }} &bull;
                {{ product.serial }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-col>
          <v-col cols="2" class="d-flex justify-end">
            <v-btn
              color="primary"
              class="ma-2"
              style="height: 30px;"
            >
              ТК
            </v-btn>
          </v-col>
        </v-row>
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
