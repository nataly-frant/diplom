<template>
  <v-list dense>
    <v-subheader>Справочники</v-subheader>

    <v-list-item
      v-for="(item, index) in infoItems"
      :key="index"
      :to="item.to"
      link
    >
      <v-list-item-title>{{ item.title }}</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

<script setup>
const infoItems = [
  {title: "Производственные линии", to: "/info-cards/production-lines"},
  {title: "Технологические карты", to: "/info-cards/technological-cards"},
  {title: "Готовая продукция", to: "/info-cards/finished-products"},
  {title: "Сырье и материалы", to: "/info-cards/raw-materials"},
  {title: "Тех. обслуживание", to: "/info-cards/maintenance"},
  {title: "Онбординг и обучение", to: "/info-cards/onboarding"},
  {title: "Нормативная документация", to: "/info-cards/standards"}
]
</script>
