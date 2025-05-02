<template>
  <div class="info-cards-page">
    <h1 class="page-title">Справочники</h1>
    <div class="links-list">
      <router-link
        v-for="(item, index) in links"
        :key="index"
        :to="item.to"
        class="link-item"
      >
        {{ item.title }}
      </router-link>
    </div>
  </div>
</template>

<script setup>
const links = [
  { title: "Производственные линии", to: "/info-cards/production-lines" },
  { title: "Технологические карты", to: "/info-cards/technological-cards" },
  { title: "Готовая продукция", to: "/info-cards/finished-products" },
  { title: "Сырье и материалы", to: "/info-cards/raw-materials" },
  { title: "Тех. обслуживание", to: "/info-cards/maintenance" },
  { title: "Онбординг и обучение", to: "/info-cards/onboarding" },
  { title: "Нормативная документация", to: "/info-cards/standards" }
]
</script>

<style scoped>
.info-cards-page {
  padding: 1rem;
}

.page-title {
  font-size: 24px;
  margin-bottom: 1rem;
}

.links-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.link-item {
  display: block;
  padding: 8px 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-decoration: none;
  color: #333;
  background-color: #f9f9f9;
  transition: background-color 0.2s, color 0.2s;
  width: 350px;
}

.link-item:hover {
  background-color: #e0e0e0;
  color: #000;
}
</style>
