<template>
  <v-container class="pa-4">
    <v-card class="mx-auto" max-width="900" elevation="4">
      <v-img
        src="https://101tea.ru/upload/resize_cache/iblock/51e/529_529_118ade429667f31b699080c7cadfe31a8/d44j0xf48mu1y9a5r81y9zyh8mfe3l58.jpg"
        height="400"
        contain
      ></v-img>

      <v-card-title class="text-h5">
        {{ demoData.name }}
      </v-card-title>

      <v-card-subtitle>Артикул: {{ demoData.article }}</v-card-subtitle>

      <v-card-text>
        <p><strong>Категория:</strong> {{ demoData.category }}</p>
        <p><strong>Происхождение:</strong> {{ demoData.origin }}</p>
        <p><strong>Форма выпуска:</strong> {{ demoData.form }}</p>
        <p><strong>Фасовка:</strong> {{ demoData.weight }}</p>
        <p><strong>Вкус:</strong> {{ demoData.taste }}</p>
        <p><strong>Условия хранения:</strong> {{ demoData.storage_condition }}</p>
        <p><strong>Методы контроля качества:</strong> {{ demoData.quality_control }}</p>
        <p><strong>ГОСТ / ТУ:</strong> {{ demoData.gost }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, computed } from 'vue'

// Получаем ID из маршрута
const route = useRoute()
const id = computed(() => route.params.id)

// Демонстрационные данные
const demoData = ref({
  name: "Черный чай",
  article: id.value,
  category: "Чай",
  origin: "Шри-Ланка",
  form: "Листовой, среднелистовой",
  weight: "50 г, 100 г, 250 г, 500 г",
  taste: "Крепкий, терпкий, без посторонних привкусов",
  storage_condition: "В сухом, прохладном месте, при температуре от 0 до +25°C, относительной влажности не выше 70%",
  quality_control: "Органолептический анализ, проверка влажности, посторонних включений",
  gost: "ГОСТ 1938-90 или ТУ, в зависимости от производителя"
})
</script>
