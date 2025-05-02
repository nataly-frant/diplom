<template>
  <div>
    <template v-if="isLoginPage">
      <!-- Только страница логина без оболочки -->
      <router-view/>
    </template>
    <template v-else>
      <!-- Полная оболочка для авторизованной части -->
      <v-app>
        <v-app-bar app color="primary" dark>
          <v-app-bar-title>Справочная система ООО "Юнилевер Русь"
          </v-app-bar-title>

          <v-spacer/>

          <!-- Кнопка "Users" (видна только админу) -->
          <template v-if="isAdmin">
            <v-btn icon @click="goToUsers" title="Пользователи">
              <v-icon>mdi-account-group</v-icon>
            </v-btn>
          </template>

          <v-btn icon @click="logout" title="Выход">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </v-app-bar>

        <v-navigation-drawer app permanent>

          <v-list dense class="d-flex flex-column fill-height">

            <!-- Главная -->
            <v-list-item :to="'/'" link>
              <v-list-item-title>Главная</v-list-item-title>
            </v-list-item>

            <!-- Справочники -->
            <v-list-group
              value="true"
              no-action
            >
              <template #activator="{ props }">
                <v-list-item
                  v-bind="props"
                  :to="'/info-cards'"
                  link
                >
                  <v-list-item-title>Справочники</v-list-item-title>
                </v-list-item>
              </template>

              <v-list-item
                v-for="(item, index) in infoItems"
                :key="index"
                :to="item.to"
                link
              >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>

            </v-list-group>

            <!-- Остальные пункты -->
            <v-list-item
              v-for="(item, index) in menuItems"
              :key="index"
              :to="item.to"
              link
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>

            <!-- Spacer чтобы "выдавить" версию вниз -->
            <v-spacer/>

            <!-- Версия -->
            <v-list-item>
              <v-list-item-title class="version-text">Версия 1.0 | 2025
              </v-list-item-title>
            </v-list-item>

          </v-list>
        </v-navigation-drawer>

        <v-main>
          <router-view/>
        </v-main>
      </v-app>
    </template>
  </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import {useRoute, useRouter} from 'vue-router'

const route = useRoute()
const router = useRouter()

// Определяем на какой странице мы находимся
const isLoginPage = computed(() => route.path === '/login')

// Флаг, показывающий, админ ли пользователь
const isAdmin = ref(true) // Здесь поставь логику проверки реального пользователя

const infoItems = [
  {title: "Производственные линии", to: "/info-cards/production-lines"},
  {title: "Технологические карты", to: "/info-cards/technological-cards"},
  {title: "Готовая продукция", to: "/info-cards/finished-products"},
  {title: "Сырье и материалы", to: "/info-cards/raw-materials"},
  {title: "Тех. обслуживание", to: "/info-cards/maintenance"},
  {title: "Онбординг и обучение", to: "/info-cards/onboarding"},
  {title: "Нормативная документация", to: "/info-cards/standards"}
]

const menuItems = [
  {title: "Склад сырья", to: "/raw-stock"},
  {title: "Склад готовой продукции", to: "/finished-stock"},
  {title: "Производственный план", to: "/production-plan"},
  {title: "Статусы линий", to: "/line-status"}
]

function logout() {
  // Здесь можешь добавить реальную логику выхода
  console.log('Выход из системы')
  // Например: очистка токенов, редирект на страницу входа и т.д.
  router.push('/login')
}

function goToUsers() {
  console.log('Переход на страницу пользователей')
  router.push('/users') // Переход на страницу /users
}
</script>

<style scoped>
.version-text {
  font-size: 12px;
  color: #888;
  text-align: center;
  width: 100%;
}
</style>

