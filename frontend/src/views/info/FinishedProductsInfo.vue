<template>
  <div>
    <div class="ml-4 mb-4">
      <h1>Готовая продукция</h1>
      <span>Справочная информация о выпускаемой продукции</span>
    </div>
    <div class="ml-4 mr-4">
      <v-table fixed-header>
        <thead>
        <tr>
          <th class="text-left">Наименование</th>
          <th class="text-left">Артикул</th>
          <th class="text-left">Категория</th>
          <th class="text-center pa-0">TK</th>
          <th class="text-center pa-0"></th>
          <th class="text-center pa-0">Действия</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="line in lines" :key="line.name" class="hover-row" @click="goToInfoCard(line)">
          <td>{{ line.name }}</td>
          <td>{{ line.article }}</td>
          <td>{{ line.category }}</td>
          <td class="text-center pa-0">
            <v-btn color="primary" style="height: 30px;">ТК</v-btn>
          </td>
          <td class="text-center pa-0">
            <v-btn color="primary" style="height: 30px;">Открыть</v-btn>
          </td>
          <td class="text-center pa-0">
            <v-btn style="height: 30px;">...</v-btn>
          </td>
        </tr>
        </tbody>
      </v-table>
      <v-pagination :length="4"></v-pagination>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import {useRouter} from 'vue-router'
import api from '@/api'

const router = useRouter()
const lines = ref([
  {"name": "Черный чай", "article": "BT-1449", "category": "Чай", "tk": "", "actions": ""},
  {
    "name": "Черный чай 'Эрл Грей'",
    "article": "BT-9876",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  {
    "name": "Черный чай с бергамотом",
    "article": "BT-4521",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  {
    "name": "Черный чай с чабрецом",
    "article": "BT-1530",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  // {"name": "Черный чай с вишней", "article": "BT-1625", "category": "Чай", "tk": "", "actions": ""},
  // {"name": "Черный чай с апельсином", "article": "BT-1740", "category": "Чай", "tk": "", "actions": ""},

  {"name": "Зеленый чай", "article": "GT-7845", "category": "Чай", "tk": "", "actions": ""},
  {"name": "Зеленый чай с мятой", "article": "GT-7875", "category": "Чай", "tk": "", "actions": ""},
  {
    "name": "Зеленый чай классический",
    "article": "GT-1010",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  // {"name": "Зеленый чай с лимоном", "article": "GT-1098", "category": "Чай", "tk": "", "actions": ""},
  // {"name": "Зеленый чай с жасмином", "article": "GT-1133", "category": "Чай", "tk": "", "actions": ""},
  // {"name": "Зеленый чай с имбирем", "article": "GT-1180", "category": "Чай", "tk": "", "actions": ""},

  {
    "name": "Белый чай с жасмином",
    "article": "WT-1122",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  {
    "name": "Белый чай с клубникой",
    "article": "WT-1205",
    "category": "Чай",
    "tk": "",
    "actions": ""
  },
  // {"name": "Белый чай с лотосом", "article": "WT-1240", "category": "Чай", "tk": "", "actions": ""},
  // {"name": "Белый чай с мелиссой", "article": "WT-1290", "category": "Чай", "tk": "", "actions": ""}
])

function goToInfoCard(line) {
  router.push({name: 'info-card', params: {id: line.article}})
}

onMounted(async () => {
  const response = await api.get('/info/finished-products/')
  // lines.value = response.data
})
</script>

<style scoped>
.hover-row:hover {
  background-color: #f5f5f5;
  cursor: pointer;
}
</style>
