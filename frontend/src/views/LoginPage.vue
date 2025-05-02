<template>
  <v-container fluid class="login-page" style="padding: 0;">
    <v-row no-gutters class="fill-height">

      <!-- Левая часть -->
      <v-col cols="12" md="6" class="left-side">
        <div class="branding-container">
          <div class="branding-center">
          <div class="branding">
            <h1>Справочная информационная система<br>для автоматизации выпуска готовой продукции</h1>
          </div>
          </div>
          <div class="footer">
            © 2025 ООО "Юнилевер Русь". Все права защищены.
          </div>
        </div>
      </v-col>

      <!-- Правая часть -->
      <v-col cols="12" md="6" class="right-side">
        <v-card class="login-card" flat>
          <v-card-text>
            <h2 class="login-title">Вход в систему</h2>

            <v-form @submit.prevent="login">
              <v-text-field
                v-model="username"
                label="Логин или табельный номер"
                outlined
                dense
                required
              />
              <v-text-field
                v-model="password"
                label="Пароль"
                type="password"
                outlined
                dense
                required
              />

              <v-btn type="submit" color="primary" block class="mt-4">
                ВОЙТИ
              </v-btn>

              <div class="additional-links mt-2">
                <router-link to="/forgot-password">Забыли пароль?</router-link>
              </div>

              <div class="support-contact mt-2">
                Техническая поддержка: <a href="mailto:support@unilever.ru">support@unilever.ru</a>
              </div>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>

    </v-row>
  </v-container>
</template>

<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')

function login() {
  console.log('Вход:', username.value, password.value)
  // Здесь должна быть реальная логика авторизации

  // Для примера: после логина переход на главную
  router.push('/')
}
</script>

<style scoped>
.login-page {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f7fa;
  overflow: hidden;
}

.left-side {
  background-color: #1976d2;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 2rem;
  height: 100%;
}

.branding-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  width: 100%;
}

.branding-center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.branding {
  text-align: center;
}

.branding h1 {
  font-size: 32px;
  margin-bottom: 1rem;
}

.branding p {
  font-size: 18px;
  line-height: 1.5;
}

.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.login-card {
  width: 100%;
  max-width: 400px;
  padding: 2rem;
}

.login-title {
  text-align: center;
  margin-bottom: 2rem;
}

.additional-links {
  text-align: center;
}

.support-contact {
  font-size: 12px;
  text-align: center;
  color: #888;
}

.footer {
  text-align: center;
  font-size: 12px;
  color: #cfd8dc;
  padding: 1rem 0;
}
</style>
